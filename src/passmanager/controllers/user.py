import os

from passmanager.models.user import User
from passmanager.models.password import Password
from passmanager.services.crypto import CryptoService
from passmanager.services.master_password import (
    ask_master_password,
    compare_master_password,
)


class UserController:
    @staticmethod
    def register(username: str) -> None:
        password = ask_master_password(username)

        password, salt = CryptoService.hash_master_password(username, password)

        User.create(username=username, password=password, salt=salt)
        print(f"--> user {username} successfully created")

    @staticmethod
    def delete(username: str) -> None:
        password = ask_master_password(username)

        # TODO
        # ADD THE ENCRYPTION

        if compare_master_password(username, password):
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
