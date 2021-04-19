import sys
import randpass2
import subprocess

def adduser(user, passwd, fname):
    '创建用户，添加密码，信息写入文件'
    # 判断用户是否存在，如果存在则退出
    result = subprocess.run(f'id {user} &> /dev/null', shell=True)
    if result.returncode == 0:
        print('用户已存在。')
        exit(101)  # 程序遇到exit函数将会彻底退出，$?指定为1

    # 创建用户，添加密码
    subprocess.run(f'useradd {user}', shell=True)
    subprocess.run(f'echo {passwd} | passwd --stdin {user}', shell=True)

    # 用户信息写入文件
    info = f'username: {user}\npassword: {passwd}\n\n'
    with open(fname, 'a') as fobj:  # a表示以追加的模式打开文件
        fobj.write(info)

if __name__ == '__main__':
    user = sys.argv[1]
    passwd = randpass2.mk_pwd()
    fname = sys.argv[2]
    adduser(user, passwd, fname)
