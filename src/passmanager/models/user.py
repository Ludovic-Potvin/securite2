import base64
from peewee import DoesNotExist, TextField

from passmanager.database import BaseModel


class User(BaseModel):
    username: TextField = TextField(primary_key=True)
    password: TextField = TextField(null=False)
    salt: TextField = TextField(null=False)

    def get_salt(self):
        return base64.b64decode(str(self.salt))
