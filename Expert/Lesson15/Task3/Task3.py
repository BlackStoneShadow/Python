import argparse
from module import Users

parser = argparse.ArgumentParser(description='ProjectUser argument parser')
parser.add_argument('-l', metavar='login', type=str, nargs='?', help='press login name')parser.add_argument('-i', metavar='id', type=str, nargs='?', help='press login id', default='0')parser.add_argument('-a', metavar='name', type=str, nargs=3, help='add user(name,level,id)', default=None)parser.add_argument('-s', metavar='show', type=str, nargs='?', help='show users', default=None)args = parser.parse_args()   users = Users.ProjectUser() 
users.login_2_sys(args.l, args.i)

if args.a is not None:
    users.add_user(*args.a)
elif args.s is not None:
    print(users)