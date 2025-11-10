from argparse import Namespace

from passmanager.controller import Controller


def launch_command(args: Namespace) -> None:
    try:
        if args.register:
            register_user(args.register)
        if args.user:
            if args.add:
                print("add")
            elif args.secure:
                print("secure")
    except:
        pass
