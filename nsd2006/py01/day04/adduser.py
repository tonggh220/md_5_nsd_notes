import sys
import randpass2
import subprocess

def adduser(user, passwd, fname):
    # 判断用户是否已存在，如果已存在，则退出
    result = subprocess.run('id %s &> /dev/null' % user, shell=True)
    if result.returncode == 0:
        print("用户已存在")
        exit(1)  # 程序遇到exit将会彻底结束。退出码指定为1

    # 创建用户，添加密码
    subprocess.run('useradd %s' % user, shell=True)
    subprocess.run('echo %s | passwd --stdin %s' % (passwd, user), shell=True)

    # 将用户信息写入文件
    # info = "username:%s\npassword:%s\n" % (user, passwd)
    info = """username:%s
password:%s
""" % (user, passwd)
    with open(fname, 'a') as fobj:  # a表示追加模式打开
        fobj.write(info)

if __name__ == '__main__':
    user = sys.argv[1]
    fname = sys.argv[2]
    password = randpass2.mk_pwd()
    adduser(user, password, fname)
