# -*- coding: utf-8 -*-
# @Author:  Claude Manchester
# Time   : 5/5/2023 10:34 AM
from sanic_dantic import BaseModel


class GithubLoginView(BaseModel):
    type: str
    code: str
