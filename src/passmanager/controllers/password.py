from passmanager.models.password import Password
from passmanager.services.crypto import encrypte_password, decrypte_password
from passmanager.services.master_password import (
    ask_master_password,
    compare_master_password,
)


class PasswordController:
    @staticmethod
    def add(username: str, label: str, password: str) -> None:
        plain_password = ask_master_password(username)

        if compare_master_password(username, plain_password):
            # Encrypte the password
            encrypted_password, salt, iv = encrypte_password(password, plain_password)

            Password.create(
                username=username,
                password=encrypted_password,
                label=label,
                salt=salt,
                iv=iv,
            )
            print(f"--> Password {label} successfully created")
        else:
            print(f"--> Wrong password for user {username}")

    @staticmethod
    def list(username) -> None:
        passwords = Password.select().where(Password.username == username)
        print(f"List of password for {username}")
        print(f"-------------------------------")
        for password in passwords:
            print(f"* {password.label}")

    @staticmethod
    def delete(username: str, label: str) -> None:
        plain_password = ask_master_password(username)

        if compare_master_password(username, plain_password):
            Password.delete().where(
                (Password.username == username) & (Password.label == label)
            ).execute()
            print(f"--> Password {label} for user {username} successfully deleted")
        else:
            print(f"--> Wrong password for user {username}")

    @staticmethod
    def see(username, label) -> None:
        plain_master_password = ask_master_password(username)

        if compare_master_password(username, plain_master_password):
            password = Password.get(
                (Password.username == username) & (Password.label == label)
            )

            encrypted_password = password.get_password()
            salt = password.get_salt()
            iv = password.get_iv()

            plain_text_password = decrypte_password(
                encrypted_password, plain_master_password, salt, iv
            )

            print(f"--> Password {label} is: {plain_text_password}")
        else:
            print(f"--> Wrong password for user {username}")

    @staticmethod
    def general(username) -> None:
        total_passwords = Password.select().where(Password.username == username).count()

        print(f"{username} information")
        print(f"-------------------")
        print(f"total passwords: {total_passwords}")
