# -*- coding: utf-8 -*-
# @Author:  Claude Manchester
# Time   : 4/20/23 3:46 PM
# Plan/work flow
from sanic import Blueprint
from sanic_dantic import parse_params

from .common import XYBaseClass
from backend.utils.format_return import ReturnMessageEnhance as Resp
from backend.utils.authorization import xy_user_check
from backend.data_model import FlowDataGetListModel, FlowDataCreateModel
from backend.data_model import FlowDataGetDetailModel, FlowDataUpdateModel, \
    FlowDataDeleteModel

flow_bp = Blueprint('flow_bp')


class XYFlowListView(XYBaseClass):
    @xy_user_check()
    @parse_params(query=FlowDataGetListModel)
    async def get(self, request, params):
        return Resp.ok_msg('')

    @xy_user_check()
    @parse_params(query=FlowDataCreateModel)
    async def post(self, request, params):
        pass


class XYFlowItemView(XYBaseClass):
    @xy_user_check()
    @parse_params(query=FlowDataGetDetailModel)
    async def get(self, request, params):
        pass

    @xy_user_check()
    @parse_params(query=FlowDataUpdateModel)
    async def put(self, request, params):
        pass

    @xy_user_check()
    @parse_params(query=FlowDataDeleteModel)
    async def delete(self, request, params):
        pass


flow_bp.add_route(XYFlowListView.as_view(), '/flow/list')
flow_bp.add_route(XYFlowItemView.as_view(), '/flow/{id}')
