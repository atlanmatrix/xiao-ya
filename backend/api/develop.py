# -*- coding: utf-8 -*-
# @Author:  Claude Manchester
# Time   : 4/20/23 5:07 PM
from sanic import Blueprint
from sanic_dantic import parse_params

from .common import XYBaseClass
from backend.utils.format_return import ReturnMessageEnhance as Resp

dev_bp = Blueprint('dev_bp')


class XYStatus(XYBaseClass):
    async def get(self, request):
        return Resp.ok_msg('I am still here')


dev_bp.add_route(XYStatus.as_view(), '/status')
