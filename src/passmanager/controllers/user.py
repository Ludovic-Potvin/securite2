import base64
import os

from passmanager.models.user import User
from passmanager.models.password import Password
from passmanager.services.crypto import hash_master_password
from passmanager.services.master_password import (
    ask_master_password,
    compare_master_password,
)


class UserController:
    @staticmethod
    def register(username: str) -> None:
        password: str = ask_master_password(username)
        password_base64, salt_base64 = hash_master_password(plain_password=password)

        User.create(username=username, password=password_base64, salt=salt_base64)
        print(f"--> user {username} successfully created")

    @staticmethod
    def delete(username: str) -> None:
        plain_password = ask_master_password(username)

        if compare_master_password(username, plain_password):
            User.delete_by_id(pk=username)
            print(f"--> user {username} successfully deleted")
        else:
            print(f"--> Wrong password for user {username}")

    @staticmethod
    def list() -> None:
        users = User.select()
        print("List of users")
        print("-------------")
        for user in users:
            print(f"* {user.username}")

    @staticmethod
    def general() -> None:
        total_users = User.select().count()
        total_passwords = Password.select().count()
        default_user = os.getenv("DEFAULT_USER", "None")

        print(f"General information")
        print(f"-------------------")
        print(f"total users: {total_users}")
        print(f"total passwords: {total_passwords}")
        print(f"default user: {default_user}")
