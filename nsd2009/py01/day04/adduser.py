import sys
import randpass2
import subprocess

def adduser(user, passwd, fname):
    "创建用户user、添加密码passwd。信息写入文件fname"
    # 判断用户是否存在，如果已存在，则退出
    result = subprocess.run('id %s &> /dev/null' % user, shell=True)
    if result.returncode == 0:
        print("用户已存在。")
        exit(1)  # 退出码$?设置为1。程序遇到exit就会彻底结束

    # 创建用户、添加密码
    subprocess.run('useradd %s' % user, shell=True)
    subprocess.run(
        'echo %s | passwd --stdin %s' % (passwd, user),
        shell=True
    )

    # 将用户信息写入文件
    info = "username:%s\npassword:%s\n" % (user, passwd)
    with open(fname, 'a') as fobj:  # 以a追加的方式打开文件
        fobj.write(info)

if __name__ == '__main__':
    user = sys.argv[1]
    passwd = randpass2.mk_pwd()
    fname = sys.argv[2]
    adduser(user, passwd, fname)
