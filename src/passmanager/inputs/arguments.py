import argparse


def parse_arguments() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        prog="passmanager",
        description="Password manager CLI",
    )

    # User management
    parser.add_argument("-r", "--register", help="Register")

    # Password management
    parser.add_argument("-u", "--user", help="Username")
    parser.add_argument("-a", "--add", help="Add password")
    parser.add_argument("-s", "--see", help="See")

    # Shared
    parser.add_argument("-l", "--list", help="List", action="store_true")
    parser.add_argument("-d", "--delete", help="Delete")

    args: argparse.Namespace = parser.parse_args()

    return args
