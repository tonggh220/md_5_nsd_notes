import sys
import randpass
import subprocess

def add_user(username, password, fname):
    # 判断用户是否存在，已存在则退出
    result = subprocess.run('id %s &> /dev/null' % username, shell=True)
    if result.returncode == 0:   # 相当于$?的值是0
        print("用户已存在。")
        exit(1)   # 程序遇到exit将会彻底结束。数字1是退出码，即$?的值

    # 创建用户，设置密码
    subprocess.run('useradd %s' % username, shell=True)
    subprocess.run(
        'echo %s | passwd --stdin %s' % (password, username), shell=True
    )

    # 用户信息写入文件
    info = 'username:%s\npassword:%s\n' % (username, password)
    with open(fname, 'a') as fobj:   # a表示追加方式打开文件
        fobj.write(info)

if __name__ == '__main__':
    username = sys.argv[1]
    fname = sys.argv[2]
    password = randpass.mk_pwd()
    add_user(username, password, fname)

# cp ../day03/randpass3.py randpass.py

