import sys
import randpass3
import subprocess

def adduser(user, passwd, fname):
    # 如果用户已存在，则退出
    result = subprocess.run(f'id {user} &> /dev/null', shell=True)
    if result.returncode == 0:
        print('用户已存在。')
        exit(1)   # 程序遇到exit函数就会彻底结束，1是退出码，默认为0

    # 创建用户，设置密码
    subprocess.run(f'useradd {user}', shell=True)
    subprocess.run(f'echo {passwd} | passwd --stdin {user}', shell=True)

    # 用户信息写入文件
    info = f'username:{user}\npassword:{passwd}\n'
    with open(fname, 'a') as fobj:  # a表示以追加的方式打开文件
        fobj.write(info)

if __name__ == '__main__':
    user = sys.argv[1]
    passwd = randpass3.mk_pwd()
    fname = sys.argv[2]
    adduser(user, passwd, fname)
