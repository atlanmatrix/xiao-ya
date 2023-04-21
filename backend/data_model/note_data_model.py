# -*- coding: utf-8 -*-
# @Author:  Claude Manchester
# Time   : 2023/4/20 16:13
from typing import Optional

from sanic_dantic import BaseModel, Field


class NoteDataCreateModel(BaseModel):
    title: str
    subtitle: Optional[str]
    content: str
    category: Optional[int]
    tags: Optional[list[str]]
    format: int
    user_id: int


class NoteDataDeleteModel(BaseModel):
    pass


class NoteDataUpdateModel(BaseModel):
    pass


class NoteDataGetListModel(BaseModel):
    title: Optional[str]
    subtitle: Optional[str]
    content: Optional[str]
    page: Optional[int] = Field(default=1)
    limit: Optional[int] = Field(default=10)


class NoteDataGetDetailModel(BaseModel):
    pass
