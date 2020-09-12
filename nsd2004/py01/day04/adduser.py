import sys
import randpass3
import subprocess

def adduser(username, password, fname):
    # 判断用户是否存在，如果存在则退出
    result = subprocess.run('id %s &> /dev/null' % username, shell=True)
    if result.returncode == 0:
        print('用户已存在')
        exit(1)  # 程序遇到exit将会彻底结束, 退出码，即$?设置为1

    # 创建用户，设置密码
    subprocess.run('useradd %s' % username, shell=True)
    subprocess.run(
        'echo %s | passwd --stdin %s' % (password, username),
        shell=True
    )

    # 将用户信息写入文件
    info = """user information:
username: %s
password: %s
""" % (username, password)
    with open(fname, 'a') as fobj:
        fobj.write(info)

if __name__ == '__main__':
    username = sys.argv[1]
    password = randpass3.mk_pwd()
    fname = sys.argv[2]
    adduser(username, password, fname)

# python3 adduser.py tom /tmp/users.txt
