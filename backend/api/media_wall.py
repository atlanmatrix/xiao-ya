# -*- coding: utf-8 -*-
# @Author:  Claude Manchester
# Time   : 4/20/23 3:48 PM
from sanic import Blueprint
from sanic_dantic import parse_params

from backend.utils.authorization import xy_user_check
from backend.data_model import MediaWallDataGetListModel, \
    MediaWallDataCreateModel
from backend.data_model import MediaWallDataGetDetailModel, \
    MediaWallDataUpdateModel, MediaWallDataDeleteModel
from .common import XYBaseClass

media_wall_bp = Blueprint('media_wall_bp')


class MediaDataManageTool:
    """
    Manage media data whether the content is local or online
    """
    def retrieve_local_media(self):
        pass

    def upload_local_media(self):
        pass

    def retrieve_online_media(self):
        pass


class MediaDataSecurityTool:
    """
    Backup, restore and check media data
    """
    def backup_media(self):
        pass

    def check_media_hash(self):
        pass

    def restore_media(self):
        pass


class XYMediaWallListView(XYBaseClass):
    @xy_user_check()
    @parse_params(query=MediaWallDataGetListModel)
    async def get(self, request, params):
        pass

    @xy_user_check()
    @parse_params(query=MediaWallDataCreateModel)
    async def post(self, request, params):
        pass


class XYMediaWallItemView(XYBaseClass):
    @xy_user_check()
    @parse_params(query=MediaWallDataGetDetailModel)
    async def get(self, request, params):
        pass

    @xy_user_check()
    @parse_params(query=MediaWallDataUpdateModel)
    async def put(self, request, params):
        pass

    @xy_user_check()
    @parse_params(query=MediaWallDataDeleteModel)
    async def delete(self, request, params):
        pass


media_wall_bp.add_route(XYMediaWallListView.as_view(), '/media_wall/list')
media_wall_bp.add_route(XYMediaWallItemView.as_view(), '/media_wall/{id}')
