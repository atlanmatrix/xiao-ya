# -*- coding: utf-8 -*-
# @Author:  Claude Manchester
# Time   : 2023/3/13 16:51

from datetime import datetime

from sqlalchemy import Column, Integer, VARCHAR, TEXT, JSON, TIMESTAMP, ARRAY
from sqlalchemy.orm import declarative_base

Base = declarative_base()


class NoteModel(Base):
    __tablename__ = "xy_note"

    id = Column(Integer, primary_key=True)
    title = Column(VARCHAR(255), default='Untitled')
    subtitle = Column(VARCHAR(255), default='')
    content = Column(TEXT, default='')
    category = Column(Integer, default=-1)
    tags = Column(ARRAY(VARCHAR(12)), default=[])
    format = Column(Integer)
    create_time = Column(TIMESTAMP, default=datetime.now())
    update_time = Column(TIMESTAMP, default=datetime.now())
    user_id = Column(Integer)
    pv = Column(Integer, default=0)
    uv = Column(Integer, default=0)
    likes = Column(ARRAY(Integer), default=[0])


class NoteVersionModel(Base):
    __tablename__ = "xy_note_version"

    id = Column(Integer, primary_key=True)
    note_id = Column(Integer)
    title = Column(VARCHAR(255))
    subtitle = Column(VARCHAR(255))
    content = Column(TEXT)
    category = Column(Integer)
    tags = Column(ARRAY(VARCHAR(12)))
    create_time = Column(TIMESTAMP)
    user_id = Column(Integer)
