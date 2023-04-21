# -*- coding: utf-8 -*-
# @Author:  Claude Manchester
# Time   : 2022/11/30 10:00:00

from datetime import datetime
from typing import Dict, List, Union

from sanic.response import json as js

from backend.logs import logger


def format_db_data(records: Union[Dict, List]) -> Union[Dict, List]:
    """
    Format datetime field in db records

    Args:
        records:
            DB data with datetime field in it. If type of records is dict,
            this function will convert it to list(with single item)

    Returns:
        formatted_records:
            DB data with datetime field converted to string
            with format '%Y-%m-%d %H:%M:%S'.
            If type of records is dict, result will be a dict object,
            otherwise, result will be a list object.
    """
    if isinstance(records, dict):
        records = [records]

    formatted_records = []
    for record in records:
        for field, value in record.items():
            if isinstance(value, datetime):
                record[field] = value.strftime('%Y-%m-%d %H:%M:%S')
        formatted_records.append(record)

    if isinstance(records, dict):
        formatted_records = formatted_records[0]
    return formatted_records


class ReturnMessageEnhance:
    def __init__(self):
        super(ReturnMessageEnhance, self).__init__()

    @staticmethod
    def err_msg(msg: str = 'System error', code: int = 1):
        """
        Response error message, default code is 1

        Args:
            code:
                0    请求成功
                1    请求失败
                2    操作失败
                3    重试
                4    重试且自动刷新
                5    无权限
                55   请求参数格式错误
            msg: error message
        """
        if not isinstance(msg, str):
            msg = str(msg)
            logger.warn(f'Convert type {type(msg)} to string(rtn_err)')

        logger.error(msg)

        if '无权限' in msg:
            code = 5

        return js({
            'code': code,
            'message': msg
        })

    @staticmethod
    def ok_msg(msg: str):
        """
        Response ok message
        """
        if not isinstance(msg, str):
            msg = str(msg)
            logger.warn(f'Convert type {type(msg)} to string(rtn_ok)')

        return js({
            'code': 0,
            'message': msg
        })

    @staticmethod
    def json(data: dict, count: int):
        return js({
            'code': 0,
            'count': count,
            'data': data
        })
    