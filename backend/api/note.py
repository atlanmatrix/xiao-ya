# -*- coding: utf-8 -*-
# @Author:  Claude Manchester
# Time   : 4/20/23 3:48 PM
import traceback

from sanic import Blueprint
from sanic import Sanic
from sanic_dantic import parse_params
from sqlalchemy import func, select, insert
from sqlalchemy.ext.asyncio import async_sessionmaker

from backend.logs import logger
from backend.config import APP_NAME
from backend.utils.authorization import xy_user_check
from backend.data_model import NoteDataGetListModel, NoteDataCreateModel
from backend.data_model import NoteDataGetDetailModel, NoteDataUpdateModel, \
    NoteDataDeleteModel
from backend.models import NoteModel, NoteVersionModel
from backend.utils.format_return import ReturnMessageEnhance as Resp
from .common import XYBaseClass

note_bp = Blueprint('note_bp')


class XYNoteListView(XYBaseClass):
    @xy_user_check('nu')
    @parse_params(query=NoteDataGetListModel)
    async def get(self, request, params):
        app = Sanic.get_app(APP_NAME)

        Session = async_sessionmaker(app.ctx.engine)
        async with Session() as session:
            query = select(
                NoteModel.title,
                NoteModel.create_time
            ).limit(
                params['limit']
            ).offset(
                (params['page'] - 1) * params['limit']
            )

            _where_clause = []
            for field in ['title', 'subtitle', 'content']:
                if params[field] is not None:
                    _where_clause.append(
                        getattr(NoteModel, field).like(
                            '%' + params[field] + '%')
                    )

            cursor = await session.execute(
                select(func.count()).select_from(query.subquery()))
            count = cursor.scalar_one()

            cursor = await session.execute(query)
            note_lst = cursor.mappings().all()

            result = []
            for note in note_lst:
                note = dict(note)
                note['create_time'] = note['create_time'].strftime(
                    '%Y-%m-%d %H:%M:%S')
                result.append(note)

            return Resp.json(result, count)

    @xy_user_check()
    @parse_params(body=NoteDataCreateModel)
    async def post(self, request, params):
        app = Sanic.get_app(APP_NAME)

        Session = async_sessionmaker(app.ctx.engine)
        async with Session() as session:
            note = NoteModel(
                title=params['title'],
                subtitle=params['subtitle'],
                content=params['content'],
                category=params['category'],
                tags=params['tags'],
                format=params['format'],
                user_id=params['user_id']
            )

            session.add(note)
            try:
                await session.commit()
            except Exception as e:
                logger.error('Insert note failed')
                traceback.print_exc()
                return Resp.err_msg(str(e))
        return Resp.ok_msg('笔记保存成功')


class XYNoteItemView(XYBaseClass):
    @xy_user_check()
    @parse_params(query=NoteDataGetDetailModel)
    async def get(self, request, params):
        raise NotImplemented()

    @xy_user_check()
    @parse_params(query=NoteDataUpdateModel)
    async def put(self, request, params):
        raise NotImplemented()

    @xy_user_check()
    @parse_params(query=NoteDataDeleteModel)
    async def delete(self, request, params):
        raise NotImplemented()


note_bp.add_route(XYNoteListView.as_view(), '/note')
note_bp.add_route(XYNoteItemView.as_view(), '/note/{id}')
