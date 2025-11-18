from passmanager.models.password import Password
from passmanager.services.master_password import (
    ask_master_password,
    compare_master_password,
)


class PasswordController:
    @staticmethod
    def add(username: str, label: str, password: str) -> None:
        plain_password = ask_master_password(username)

        if compare_master_password(username, plain_password):
            # TODO
            # ADD THE DECRYPTION

            Password.create(username=username, password=password, label=label)
            print(f"--> Password {label} successfully created")
        else:
            print(f"--> Wrong password for user {username}")

    @staticmethod
    def list(username) -> None:
        passwords = Password.select(Password.username == username)
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
            password = (
                Password.select()
                .where((Password.username == username) & (Password.label == label))
                .get()
            )

            # TODO
            # ADD THE DECRYPTION
            plain_text_password = password.password

            print(f"--> Password {label} is: {plain_text_password}")
        else:
            print(f"--> Wrong password for user {username}")

    @staticmethod
    def general(username) -> None:
        total_passwords = Password.select().where(Password.username == username).count()

        print(f"{username} information")
        print(f"-------------------")
        print(f"total passwords: {total_passwords}")
