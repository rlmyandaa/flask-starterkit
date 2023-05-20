from sqlalchemy import Column, ForeignKey
from sqlalchemy.ext.declarative import declarative_base, declared_attr
from sqlalchemy.dialects.postgresql.base import INTEGER

from app.utils import camel_to_snake
from app.app import db


def id_column() -> Column:
    return Column(
        INTEGER,
        autoincrement=True,
        primary_key=True,
        nullable=False,
        unique=True
    )


def int_fk_column(foreign_key) -> Column:
    return Column(INTEGER, ForeignKey(foreign_key))

BaseModel = db.Model
