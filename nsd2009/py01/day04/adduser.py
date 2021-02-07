import sys
import randpass2

def adduser(user, passwd, fname):
    "创建用户user、添加密码passwd。信息写入文件fname"
    # 判断用户是否存在，如果已存在，则退出

    # 创建用户、添加密码

    # 将用户信息写入文件

if __name__ == '__main__':
    user = sys.argv[1]
    passwd = randpass2.mk_pwd()
    fname = sys.argv[2]
    adduser(user, passwd, fname)
