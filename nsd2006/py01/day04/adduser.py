import sys
import randpass2

def adduser(user, passwd, fname):

if __name__ == '__main__':
    user = sys.argv[1]
    fname = sys.argv[2]
    password = randpass2.mk_pwd()
    adduser(user, password, fname)
