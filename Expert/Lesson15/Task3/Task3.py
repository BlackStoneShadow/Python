import argparse
from module import Users

parser = argparse.ArgumentParser(description='ProjectUser argument parser')
parser.add_argument('-l', metavar='login', type=str, nargs='?', help='press login name')
users.login_2_sys(args.l, args.i)

if args.a is not None:
    users.add_user(*args.a)
elif args.s is not None:
    print(users)