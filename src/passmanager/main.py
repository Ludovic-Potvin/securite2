from passmanager.arguments import parse_arguments


def main() -> None:
    # DB
    # TODO validate the DB exist
    # TODO create DB if it doesn't

    # Arguments
    args = parse_arguments()

    # Launch the command
    try:
        if args.register:
            print("register")
        if args.user:
            if args.add:
                print("add")
            elif args.secure:
                print("secure")
    except:
        pass


def register_user(username: str) -> bool:
    return True


def add_password(username: str, label: str, password: str) -> bool:
    return True


def display_password(username: str, label: str) -> str:
    password = "test"
    return password
