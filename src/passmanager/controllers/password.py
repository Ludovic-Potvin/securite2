from passmanager.models.password import Password
from passmanager.services.master_password import ask_master_password


class PasswordController:
    @staticmethod
    def add(username: str, label: str, password: str) -> None:
        master_password = ask_master_password(username)

        # TODO
        # ADD THE ENCRYPTION

        Password.create(username=username, password=password, label=label)
        print(f"--> Password {label} successfully created")

    @staticmethod
    def list(username) -> None:
        passwords = Password.select(Password.username == username)
        print(f"List of password for {username}")
        print(f"-------------------------------")
        for password in passwords:
            print(f"* {password.label}")
