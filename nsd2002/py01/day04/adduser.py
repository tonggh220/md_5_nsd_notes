import sys
import randpass2
import subprocess

def adduser(user, passwd, fname):
    # 判断用户是否存在
    result = subprocess.run('id %s &> /dev/null' % user, shell=True)
    if result.returncode == 0:
        print('用户已存在')
        return   # return类似于循环的break，将会结束函数，不指定返回值，默认返回None

    # 创建用户并设置密码
    subprocess.run('useradd %s' % user, shell=True)
    subprocess.run('echo %s | passwd --stdin %s' % (passwd, user), shell=True)

    # 将用户信息写入文件
    info = "username: %s\npassword: %s\n" % (user, passwd)
    with open(fname, 'a') as fobj:  # 以a打开文件，表示追加
        fobj.write(info)

if __name__ == '__main__':
    user = sys.argv[1]
    passwd = randpass2.mk_pwd()
    fname = sys.argv[2]
    adduser(user, passwd, fname)
