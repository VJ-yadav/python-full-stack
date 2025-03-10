import reflex as rx
from datetime import datetime
from sqlmodel import Field
from .. import utils

import sqlalchemy


class BlogPostModel(rx.Model, table = True):
    title: str
    content: str
    created_at: datetime = Field(
        default_factory= utils.timing.get_utc_now,
        sa_type=sqlalchemy.DateTime(timezone=True),
        sa_column_kwargs={
            'server_default': sqlalchemy.func.now(),
        },
        nullable=False
        )
    
    updated_at : datetime = Field(
        default_factory= utils.timing.get_utc_now,
        sa_type=sqlalchemy.DateTime(timezone=True),
        sa_column_kwargs={
            'onupdate': sqlalchemy.func.now(),
            'server_default': sqlalchemy.func.now(),
        },
        nullable=False
        )
    publish_active: bool = False

    publish_date : datetime = Field(
        default = None,
        sa_type=sqlalchemy.DateTime(timezone=True),
        sa_column_kwargs={},
        nullable=True
        )
    
    