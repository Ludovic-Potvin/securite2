from peewee import CompositeKey, ForeignKeyField, TextField

from passmanager.database import BaseModel
from passmanager.models.user import User


class Password(BaseModel):
    username: ForeignKeyField = ForeignKeyField(
        User, backref="passwords", on_delete="CASCADE"
    )
    label: TextField = TextField(null=False)
    password: TextField = TextField(null=False)

    class Meta:  # pyright: ignore[reportIncompatibleVariableOverride]
        primary_key: CompositeKey = CompositeKey("username", "label")
