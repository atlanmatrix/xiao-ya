# -*- coding: utf-8 -*-
# @Author:  Claude Manchester
# Time   : 2023/2/17 10:28
import argparse
import json
import os
import sys

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from redis import Redis
from sqlalchemy.ext.asyncio import (create_async_engine)
from sanic import Sanic
from sanic.exceptions import Unauthorized
from sanic.config import Config

import backend.config as cfg
from backend.logs import logger
from backend.config import APP_NAME
from backend.api import dev_bp, note_bp, login_bp#, flow_bp, media_wall_bp
from backend.utils.custom_exception import RespInterruptHandler
from backend.utils.format_return import ReturnMessageEnhance as Resp

app = Sanic(APP_NAME, error_handler=RespInterruptHandler())
app.blueprint([
    dev_bp,
    note_bp,
    login_bp
    # flow_bp,
    # media_wall_bp,
], url_prefix='/xiaoya')


class CustomConfig(Config):
    ...


@app.listener("before_server_start")
async def init(app, loop):
    user = os.environ.get("POSTGRES_USER")
    if user is None:
        raise RuntimeError(f"环境变量 **POSTGRES_USER** 未设置")

    passwd = os.environ.get("POSTGRES_PASSWORD")
    if passwd is None:
        raise RuntimeError(f"环境变量 **POSTGRES_PASSWORD** 未设置")

    app.ctx.pg_user = user
    app.ctx.pg_passwd = passwd


@app.listener("after_server_start")
async def start(app, loop):
    init_db_engine()
    init_redis()


def init_db_engine():
    url = f"postgresql+asyncpg://{app.ctx.pg_user}:{app.ctx.pg_passwd}@" \
          f"{cfg.PG_CONFIG.host}:{cfg.PG_CONFIG.port}/" \
          f"{cfg.PG_CONFIG.db_map.xiaoya}"

    app.ctx.engine = create_async_engine(url)


def init_redis():
    app.ctx.redis = Redis(
        host=cfg.REDIS_CONFIG['host'],
        port=cfg.REDIS_CONFIG['port'],
        db=cfg.REDIS_CONFIG['db'],
        decode_responses=True
    )


@app.listener("before_server_stop")
async def shutdown(app, loop):
    ...


@app.middleware('request')
async def halt_request(request):
    logger.debug(request.path)
    for path in ['status', 'login']:
        if request.path.startswith(f'/xiaoya/{path}'):
            logger.debug(f'request path {path} in white list')
            return

    token = request.cookies.get('access_token')
    if not token:
        logger.debug('not login yet')
        raise Unauthorized('尚未登录')

    r_client = app.ctx.redis
    user_info = r_client.get(f'UserInfo:{token}')

    if user_info is None:
        logger.debug('login info has expired')
        raise Unauthorized('登录已过期')

    logger.debug('login info still valid')
    request.headers.user_info = json.loads(user_info)
    r_client.expire(f'UserInfo:{token}', cfg.USER_EXPIRE_TIME)
    return


def main():
    parser = argparse.ArgumentParser(description='XiaoYa intelligence server')
    parser.add_argument(
        '-p', '--port',
        type=int,
        default=2305,
        help='Port to run app on (default 2305)'
    )
    parser.add_argument(
        '-d', '--debug',
        action='store_true',
        default=False,
        help='Run the application in debug mode (reloads when the source '
             'changes and gives more detailed error messages)'
    )
    parser.add_argument(
        '-w', '--workers',
        type=int,
        default=1,
        help='workers to run app  (default 1)'
    )
    parser.add_argument(
        '-c', '--cfg',
        default=None,
        help='配置文件json/yaml'
    )
    args = parser.parse_args()

    debug = True if args.debug else False
    auto_reload = True if debug else False,
    workers = args.workers if args.workers else 1

    app.run(
        host="0.0.0.0",
        port=args.port,
        dev=debug,
        debug=debug,
        auto_reload=auto_reload,
        access_log=True,
        workers=workers)


if __name__ == '__main__':
    main()
