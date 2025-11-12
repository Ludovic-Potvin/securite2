from argparse import Namespace

from passmanager.controllers.password import PasswordController
from passmanager.controllers.user import UserController


def launch_command(args: Namespace) -> None:
    try:
        if args.user:
            if args.add:
                print("add")
            elif args.delete:
                print("delete password")
            elif args.see:
                print("see")
            elif args.list:
                username: str = args.user
                PasswordController.list(username)
            else:
                print("general user info")
        else:
            if args.register:
                username: str = args.register
                UserController.register(username)
            elif args.delete:
                username: str = args.delete
                UserController.delete(username)
            elif args.list:
                UserController.list()
            else:
                UserController.general()
    except:
        pass
