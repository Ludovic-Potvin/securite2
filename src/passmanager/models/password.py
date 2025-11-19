import base64
from peewee import CompositeKey, DoesNotExist, ForeignKeyField, TextField

from passmanager.database import BaseModel
from passmanager.models.user import User


class Password(BaseModel):
    username: ForeignKeyField = ForeignKeyField(
        User, backref="passwords", on_delete="CASCADE"
    )
    label: TextField = TextField(null=False)
    password: TextField = TextField(null=False)
    salt: TextField = TextField(null=False)
    iv: TextField = TextField(null=False)

    class Meta:  # pyright: ignore[reportIncompatibleVariableOverride]
        primary_key: CompositeKey = CompositeKey("username", "label")

    def get_salt(self):
        return base64.b64decode(str(self.salt))

    def get_iv(self):
        return base64.b64decode(str(self.iv))

    def get_password(self):
        return base64.b64decode(str(self.password))
