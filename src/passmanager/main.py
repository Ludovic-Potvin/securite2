from argparse import Namespace
from passmanager.arguments import parse_arguments
from passmanager.database import db
from passmanager.models.user import User
from passmanager.models.password import Password
from dotenv import load_dotenv
from passmanager.commands import launch_command

load_dotenv()


def main() -> None:
    args: Namespace = parse_arguments()

    init_db()

    try:
        launch_command(args)
        pass
    finally:
        close_db()


def init_db() -> None:
    db.connect()
    db.create_tables(  # pyright: ignore[reportUnknownMemberType]
        models=[
            User,
            Password,
        ]
    )


def close_db() -> None:
    db.close()
