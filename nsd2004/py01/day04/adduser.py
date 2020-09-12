import sys
import randpass3

def adduser(username, password, fname):

if __name__ == '__main__':
    username = sys.argv[1]
    password = randpass3.mk_pwd()
    fname = sys.argv[2]
    adduser(username, password, fname)
