import getpass

from peewee import DoesNotExist

from passmanager.models.user import User


def ask_master_password(username: str) -> str:
    prompt: str = f"/!\\ Enter {username} master password: "
    password: str = getpass.getpass(prompt=prompt)
    return password


def compare_master_password(username: str, password_input: str) -> bool:
    # Fetch the user
    try:
        user: User = User.get_by_id(pk=username)
    except DoesNotExist:
        raise ValueError(f"User '{username}' not found.")

    return True if user.password == password_input else False
