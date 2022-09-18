"""
也支持表集抽象
"""

from sqlalchemy import MetaData
from sqlalchemy import Table, Column, Integer, String, DateTime
from zoneinfo import ZoneInfo
from datetime import datetime as dt

metadata_obj = MetaData()

# 对表的字段进行约束，
user_table = Table(
    "user_account", metadata_obj, Column('id', Integer, primary_key=True),
    Column('username', String(255), nullable=False, unique=True),
    Column('password', String(255), nullable=False),
    Column('createDate', String(255), default=dt.now(), nullable=False))
"""
python shell 导入两份文件后自动生成，表结构
>>> from models import metadata_obj
>>> from database import engine
>>> metadata_obj.create_all(engine)
"""
