import sys
import randpass2
import subprocess

def adduser(user, pwd, fname):
    # 判断用户是否存在，存在则退出
    result = subprocess.run('id %s &> /dev/null' % user, shell=True)
    if result.returncode == 0:
        print("用户已存在")
        exit(1)    # $? -> 1

    # 创建用户，并设置密码
    subprocess.run('useradd %s' % user, shell=True)
    subprocess.run('echo %s | passwd --stdin %s' % (pwd, user), shell=True)

    # 将用户名和密码写入文件
    info = """username: %s
password:%s
""" % (user, pwd)
    with open(fname, 'a') as fobj:  # 以追加模式打开文件
        fobj.write(info)

if __name__ == '__main__':
    user = sys.argv[1]
    pwd = randpass2.mk_pwd()
    fname = sys.argv[2]
    adduser(user, pwd, fname)
