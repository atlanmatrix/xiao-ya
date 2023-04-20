# -*- coding: utf-8 -*-
# @Author:  Claude Manchester
# Time   : 2023/2/17 11:15

import aioredis

from backend.config import REDIS_CONFIG


class Redis:
    def __init__(self):
        ...

    async def get_user_instance(self):
        return await aioredis.create_redis_pool(
            f'redis://{REDIS_CONFIG.host}:{REDIS_CONFIG.port}',
            db=REDIS_CONFIG.DB_MAP['user'])
