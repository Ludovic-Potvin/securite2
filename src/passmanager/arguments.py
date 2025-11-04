import argparse


def parse_arguments() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        prog="passmanager",
        description="Password manager CLI",
    )

    parser.add_argument("-r", "--register", help="Register")

    parser.add_argument("-u", "--user", help="Username")
    parser.add_argument("-a", "--add", help="Add password")
    parser.add_argument("-s", "--secure", help="Secure")

    args: argparse.Namespace = parser.parse_args()

    return args
