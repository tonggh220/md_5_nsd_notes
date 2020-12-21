import paramiko
import sys
import os
import getpass

def rcmd(host, user, passwd, cmds):
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh.connect(host, username=user, password=passwd)
    stdin, stdout, stderr = ssh.exec_command(cmds)
    out = stdout.read()
    err = stderr.read()
    if out:
        print('[%s] \033[32;1mOUT\033[0m:\n%s' % (host, out.decode()))
    if err:
        print('[%s] \033[31;1mERROR\033[0m:\n%s' % (host, err.decode()))
    ssh.close()

if __name__ == '__main__':
    # 服务器地址文件和命令通过命令行提供，否则退出
    if len(sys.argv) < 3:
        print('Usage: %s ipfile commands' % sys.argv[0])
        exit(1)

    # 服务器地址文件不存在则退出
    if not os.path.isfile(sys.argv[1]):
        print('No such file:', sys.argv[1])
        exit(2)

    ipfile = sys.argv[1]
    # 将地址后面的字符串拼接成要执行的命令
    commands = ' '.join(sys.argv[2:])
    user = 'root'
    # 获取密码
    passwd = getpass.getpass()

    # 在所有远程主机上执行任务
    with open(ipfile) as fobj:
        for line in fobj:
            ip = line.strip()  # 去除行尾的\n
            rcmd(ip, user, passwd, commands)
