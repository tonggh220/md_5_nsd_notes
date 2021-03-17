import sys
import randpass3

def adduser(user, passwd, fname):
    # 如果用户已存在，则退出

    # 创建用户，设置密码

    # 用户信息写入文件

if __name__ == '__main__':
    user = sys.argv[1]
    passwd = randpass3.mk_pwd()
    fname = sys.argv[2]
    adduser(user, passwd, fname)
