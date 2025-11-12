from argparse import Namespace

from passmanager.controllers.password import PasswordController
from passmanager.controllers.user import UserController


def launch_command(args: Namespace) -> None:
    try:
        if args.user:
            if args.add:
                username: str = args.user
                label: str = args.add[0]
                password = args.add[1]
                PasswordController.add(username, label, password)
            elif args.delete:
                username: str = args.user
                label: str = args.delete
                PasswordController.delete(username, label)
            elif args.see:
                username: str = args.user
                label: str = args.see
                PasswordController.see(username, label)
            elif args.list:
                username: str = args.user
                PasswordController.list(username)
            else:
                username: str = args.user
                PasswordController.general(username)
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
    except Exception as e:
        print(e)
