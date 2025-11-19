import base64
import getpass

from peewee import DoesNotExist

from passmanager.models.user import User
from passmanager.services.crypto import hash_master_password


def ask_master_password(username: str) -> str:
    prompt: str = f"/!\\ Enter {username} master password: "
    password: str = getpass.getpass(prompt=prompt)
    return password


def compare_master_password(username: str, plain_password: str) -> bool:
    # Fetch the user
    try:
        user: User = User.get_by_id(pk=username)
    except DoesNotExist:
        raise ValueError(f"User '{username}' not found.")

    # Hash the password
    salt = user.get_salt()
    hash_input, _ = hash_master_password(plain_password, salt)

    return True if user.password == hash_input else False
