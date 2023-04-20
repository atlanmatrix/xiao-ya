# -*- coding: utf-8 -*-
# @Author:  Claude Manchester
# Time   : 2023/3/13 16:51

from sqlalchemy import Column, Integer, VARCHAR
from sqlalchemy.orm import declarative_base

Base = declarative_base()


class KubeModel(Base):
    __tablename__ = "xy_note"

    id = Column(Integer, primary_key=True)
