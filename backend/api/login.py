# -*- coding: utf-8 -*-
# @Author:  Claude Manchester
# Time   : 5/5/2023 10:25 AM
import json
import os
import random
import string
import traceback

import requests
from sanic import Sanic, Blueprint
from sanic.response import json as sanic_json
from sanic_dantic import parse_params
from sqlalchemy import select
from sqlalchemy.ext.asyncio import async_sessionmaker

from backend.config import APP_NAME, ACCOUNT_TYPE, USER_EXPIRE_TIME
from backend.data_model import GithubLoginView
from backend.logs import logger
from backend.models import UserModel
from backend.utils.authorization import xy_user_check
from backend.utils.format_return import ReturnMessageEnhance as Resp
from .common import XYBaseClass

login_bp = Blueprint('login_bp')


class GithubLoginView(XYBaseClass):
    async def get_user_info(self, access_token):
        get_user_info_url = 'https://api.github.com/user'
        headers = {
            'Authorization': f'Bearer {access_token}'
        }
        response = requests.get(get_user_info_url, headers=headers)

        if response.status_code != 200:
            return False, f'获取用户信息失败：{response.status_code}'

        resp_json = response.json()
        if 'message' in resp_json:
            return False, f'获取用户信息失败：{resp_json["message"]}'

        return True, resp_json

    async def update_user_info(self, user_info):
        app = Sanic.get_app(APP_NAME)

        Session = async_sessionmaker(app.ctx.engine)
        identify_code = str(user_info['id'])
        async with Session() as session:
            query = select(
                UserModel
            ).where(
                UserModel.identify_code == identify_code
            )

            cursor = await session.execute(query)
            user_lst = cursor.mappings().all()

        if len(user_lst) == 0:
            logger.debug('New user login')
            user = UserModel(
                account=f'github_{identify_code}',
                account_type=ACCOUNT_TYPE['github'],
                identify_code=identify_code,
                nickname=user_info.get('login'),
                email=user_info.get('email'),
                avatar=user_info.get('avatar_url'),
                description=user_info.get('bio')
            )

            async with Session() as session:
                session.add(user)
                try:
                    await session.commit()
                except Exception as e:
                    logger.error('Insert user info failed')
                    traceback.print_exc()
                    return False, e
        else:
            logger.debug('Exists user login')
        return True, ''

    async def cache_login_status(self, token, user_info):
        app = Sanic.get_app(APP_NAME)
        r_client = app.ctx.redis

        try:
            r_client.set(f'UserInfo:{token}', json.dumps(user_info))
            await r_client.expire(f'UserInfo:{token}', USER_EXPIRE_TIME)
        except Exception as e:
            logger.error('Cache user info failed')
            traceback.print_exc()
            return False, e
        return True, ''

    async def gen_token(self):
        token = ''.join([
            random.choice(string.ascii_letters + string.digits)
            for _ in range(128)
        ])

        return token

    @xy_user_check()
    @parse_params(query=GithubLoginView)
    async def get(self, request, params):
        login_type = params['type']
        code = params['code']

        if login_type != 'github':
            return Resp.err_msg('Login type invalid')

        app_id = os.environ.get('GITHUB_CLIENT_ID')
        if not app_id:
            raise RuntimeError('missing env variable `GITHUB_CLIENT_ID`')

        secrets = os.environ.get('GITHUB_SECRETS')
        if not secrets:
            raise RuntimeError('missing env variable `GITHUB_SECRETS`')

        access_token_url = 'https://github.com/login/oauth/access_token'
        response = requests.post(access_token_url, headers={
            'Accept': 'application/json'
        }, params={
            'client_id': app_id,
            'client_secret': secrets,
            'code': code
        })

        if response.status_code != 200:
            return Resp.err_msg('获取授权信息失败')

        resp_json = response.json()
        if 'error' in resp_json:
            return Resp.err_msg('授权信息不合法，请联系管理员')

        access_token = resp_json['access_token']

        g_res, user_info = await self.get_user_info(access_token)
        if not g_res:
            return Resp.err_msg(user_info)

        u_res, msg = await self.update_user_info(user_info)
        if not u_res:
            return Resp.err_msg(f'用戶信息处理失败：{msg}')

        token = await self.gen_token()
        await self.cache_login_status(token, user_info)

        response = sanic_json(({
            'code': 0,
            'message': 'Login successfully'
        }))

        response.cookies['access_token'] = token

        return response


login_bp.add_route(GithubLoginView.as_view(), '/login')
