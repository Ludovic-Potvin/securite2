class PasswordController:
    @staticmethod
    def add(username: str) -> None:
        password = ask_master_password(username)
        user: User = User.create(username=username, password=password)
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
        users = User.select().dicts()
        print("List of users")
        print("-------------")
        for user in users:
            print(f"* {user}")

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
