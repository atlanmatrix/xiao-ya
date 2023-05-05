# -*- coding: utf-8 -*-
# @Author:  Claude Manchester
# Time   : 5/5/2023 11:02 AM
from datetime import datetime

from sqlalchemy import Column, Integer, VARCHAR, TIMESTAMP
from sqlalchemy.orm import declarative_base

Base = declarative_base()


class UserModel(Base):
    __tablename__ = "xy_user"

    id = Column(Integer, primary_key=True)
    account = Column(VARCHAR(255), default='')
    account_type = Column(Integer)
    identify_code = Column(VARCHAR(255), default='')
    nickname = Column(VARCHAR(255), default='')
    phone = Column(VARCHAR(11), default='')
    email = Column(VARCHAR(255), default='')
    avatar = Column(VARCHAR(255), default='')
    description = Column(VARCHAR(255), default='')
    gender = Column(Integer)
    create_time = Column(TIMESTAMP, default=datetime.now())
    update_time = Column(TIMESTAMP, default=datetime.now())
