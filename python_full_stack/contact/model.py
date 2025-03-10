import reflex as rx
import asyncio
import sqlalchemy

from datetime import datetime, timezone
from sqlmodel import Field
from .. import utils

class ContactEntryModel(rx.Model, table = True):
    user_id: int = Field(nullable=True)
    first_name: str
    middle_name: str = Field(nullable=True)
    last_name: str 
    email:str
    message:str
    created_at: datetime = Field(
        default_factory= utils.timing.get_utc_now,
        sa_type=sqlalchemy.DateTime(timezone=True),
        sa_column_kwargs={
            'server_default': sqlalchemy.func.now(),
        },
        nullable=False
        )