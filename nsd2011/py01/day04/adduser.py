import sys
import randpass2

def adduser(user, passwd, fname):
    '创建用户，添加密码，信息写入文件'

if __name__ == '__main__':
    user = sys.argv[1]
    passwd = randpass2.mk_pwd()
    fname = sys.argv[2]
    adduser(user, passwd, fname)
