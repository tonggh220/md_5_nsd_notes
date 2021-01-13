import sys
import randpass2

def adduser(user, passwd, fname):
    "创建用户user，添加密码passwd，信息写到fname文件中"

if __name__ == '__main__':
    username = sys.argv[1]
    password = randpass2.mk_pwd()
    fname = sys.argv[2]
    adduser(username, password, fname)
