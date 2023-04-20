# -*- coding: utf-8 -*-
# @Author:  Claude Manchester
# Time   : 2023/2/17 10:38
class EnhancedDict(dict):
    __getattr__ = dict.get
    __setattr__ = dict.__setitem__
    __delattr__ = dict.__delitem__


APP_NAME = "XiaoYa"

LOG_FILE = "/opt/logs/xiaoya.log"
LOG_LEVEL = "DEBUG"

# PostgresSQL connect information and DBs
PG_CONFIG = EnhancedDict({
    "host": "127.0.0.1",
    "port": 15432,
    "db_map": EnhancedDict({
        "xiaoya": "xiaoya",
    })
})

# Redis connect information and DBs
REDIS_CONFIG = EnhancedDict({
    "host": "127.0.0.1",
    "port": 6379,
    "user_cache_db": 1,
})
