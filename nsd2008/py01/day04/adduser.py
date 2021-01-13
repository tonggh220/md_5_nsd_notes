import sys
import randpass2
import subprocess

def adduser(user, passwd, fname):
    "创建用户user，添加密码passwd，信息写到fname文件中"
    # 如果用户已存在，则退出
    result = subprocess.run(
        'id %s &> /dev/null' % user, shell=True
    )
    if result.returncode == 0:
        print("用户已存在")
        exit(101)  # 程序遇到exit()就会结束

    # 创建用户，加密码
    subprocess.run('useradd %s' % user, shell=True)
    subprocess.run(
        'echo %s | passwd --stdin %s' % (passwd, user),
        shell=True
    )

    # 写入用户信息到文件
    info = 'username:%s\npassword:%s\n' % (user, passwd)
    with open(fname, 'a') as fobj:  # a表示追加
        fobj.write(info)

if __name__ == '__main__':
    username = sys.argv[1]
    password = randpass2.mk_pwd()
    fname = sys.argv[2]
    adduser(username, password, fname)
