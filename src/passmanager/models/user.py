from peewee import TextField

from passmanager.database import BaseModel


class User(BaseModel):
    username: TextField = TextField(primary_key=True)
    password: TextField = TextField(null=False)
    salt: TextField = TextField(null=False)
