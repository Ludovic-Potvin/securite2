from argparse import Namespace
from passmanager.arguments import parse_arguments
from passmanager.db import init_db
from dotenv import load_dotenv
from passmanager.commands import launch_command

load_dotenv()


def main() -> None:
    init_db()
    args: Namespace = parse_arguments()
    launch_command(args)
