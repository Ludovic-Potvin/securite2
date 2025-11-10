from argparse import Namespace

from passmanager.controller import Controller


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
                print("list password")
            else:
                print("general user info")
        else:
            if args.register:
                print("delete user")
            elif args.delete:
                print("delete user")
            elif args.list:
                print("list users")
            else:
                print("general users info")
    except:
        pass
