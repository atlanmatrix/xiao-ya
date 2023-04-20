# -*- coding: utf-8 -*-
# @Author:  Claude Manchester
# Time   : 2022/12/1 10:31

from sanic.handlers import ErrorHandler

from backend.utils.format_return import ReturnMessageEnhance as Resp


class RespInterrupt(Exception):
    """
    If you want to response error message from a function which is called by
    request handler, raise a `RespInterrupt` exception may be a better way than
    return step by step.

    This exception will return a `sanic.response` object which will be caught
    by `RespInterruptHandler` later, and finally behaviours like a normal
    response.
    """
    def __init__(self, msg, code=1):
        super().__init__(msg)
        self.resp = Resp.err_msg(msg, code)


class RespInterruptHandler(ErrorHandler):
    """
    This handler will catch `RespInterrupt` exception and convert it to a
    normal `sanic.response` object.
    """
    def default(self, request, exception):
        if isinstance(exception, RespInterrupt):
            return exception.resp
        return super().default(request, exception)
