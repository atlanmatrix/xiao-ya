# -*- coding: utf-8 -*-
# @Author:  Claude Manchester
# Time   : 4/20/23 3:48 PM
from sanic import Blueprint
from sanic_dantic import parse_params

from backend.utils.authorization import xy_user_check
from backend.data_model import NoteDataGetListModel, NoteDataCreateModel
from backend.data_model import NoteDataGetDetailModel, NoteDataUpdateModel, \
    NoteDataDeleteModel
from .common import XYBaseClass

note_bp = Blueprint('note_bp')


class XYNoteListView(XYBaseClass):
    @xy_user_check()
    @parse_params(query=NoteDataGetListModel)
    async def get(self, request, params):
        raise NotImplemented()

    @xy_user_check()
    @parse_params(query=NoteDataCreateModel)
    async def post(self, request, params):
        raise NotImplemented()


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


note_bp.add_route(XYNoteListView.as_view(), '/note/list')
note_bp.add_route(XYNoteItemView.as_view(), '/note/{id}')
