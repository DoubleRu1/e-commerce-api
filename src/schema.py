from typing import Optional
from sqlmodel import SQLModel, Field
class Hero(SQLModel, table=True):
    id : Optional[int] = Field(default=None, primary_key=True)  # default=None表示该字段默认值为None，主键会在插入数据库时自动生成；primary_key=True表示这是主键
    name : str = Field(index=True)  # index=True表示在数据库中为该字段创建索引，加快根据name字段的查询速度
    age : Optional[int] = Field(default=None,index=True)
    