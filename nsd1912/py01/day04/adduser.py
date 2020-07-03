import sys
import mk_pwd2
import subprocess

def add_user(user, passwd, fname):
    # 判断用户是否存在，存在则直接返回
    result = subprocess.run('id %s &> /dev/null' % user, shell=True)
    if result.returncode == 0:
        print('用户已存在。')
        return    # return类似于循环的break，遇到return函数提前结束，默认返回None

    # 创建用户，添加密码
    subprocess.run('useradd %s' % user, shell=True)
    subprocess.run('echo %s | passwd --stdin %s' % (passwd, user), shell=True)

    # 将用户名和密码写入文件
    info = "用户名: %s\n密码: %s\n" % (user, passwd)
    with open(fname, 'a') as fobj:
        fobj.write(info)

if __name__ == '__main__':
    user = sys.argv[1]
    fname = sys.argv[2]
    passwd = mk_pwd2.mk_pwd()
    add_user(user, passwd, fname)
