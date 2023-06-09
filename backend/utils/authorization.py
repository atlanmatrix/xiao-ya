# -*- coding: utf-8 -*-
# @Author:  Claude Manchester
# Time   : 4/20/23 3:51 PM
from sanic.exceptions import Forbidden


# Normal user, Operator, Maintainer
USER_TYPE = {
    'nu': 1,
    'op': 2,
    'mt': 3
}


def xy_user_check(*user_type_lst):
    def decorate(func):
        async def wrapper(_, request, *args, **kwargs):
            return await func(_, request, *args, **kwargs)

        return wrapper

    return decorate


class GithubAuth:
    pass
