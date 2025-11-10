import getpass
from typing import Any
from passmanager.models.user import User
from passmanager.database import db

from peewee import DoesNotExist


class Controller:
    @staticmethod
    def register_user(username: str, password: str) -> User:
        user: User = User.create(username=username, password=password)
        return user

    @staticmethod
    def delete_user(username: str) -> bool:
        is_deleted: bool = User.delete_by_id(pk=username)
        return is_deleted


def _ask_master_password(username) -> str:
    prompt: str = f"/!\\ Enter {username} master password: "
    password: str = getpass.getpass(prompt=prompt)
    return password


def _compare_user_password(username: str, password_input: str) -> bool:
    # Fetch the user
    try:
        user: User = User.get_by_id(pk=username)
    except DoesNotExist:
        raise ValueError(f"User '{username}' not found.")

    # Encode the password input
    # TODO ENCODE
    encoded_input = password_input

    return True if user.password == encoded_input else False
