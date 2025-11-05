from argparse import Namespace
from passmanager.models import User, Password

def launch_command(args: Namespace) -> None:
    try:
        if args.register:
            register_user(args)
        if args.user:
            if args.add:
                print("add")
            elif args.secure:
                print("secure")
    except:
        pass

def register_user(args: Namespace) -> None:
    

