import sys
import randpass

def add_user(username, password, fname):


if __name__ == '__main__':
    username = sys.argv[1]
    fname = sys.argv[2]
    password = randpass.mk_pwd()
    add_user(username, password, fname)

# cp ../day03/randpass3.py randpass.py

