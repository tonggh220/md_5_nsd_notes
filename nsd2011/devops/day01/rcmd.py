import paramiko
import sys
import os
import threading
import getpass

def rcmd(host, port=22, user='root', passwd=None, cmds=None):
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh.connect(host, port=port, username=user, password=passwd)
    stdin, stdout, stderr = ssh.exec_command(cmds)
    out = stdout.read()
    err = stderr.read()
    if out:
        print(f'[{host}] \033[32;1mOUT\033[0m:\n{out.decode()}')
    if err:
        print(f'[{host}] \033[31;1mERROR\033[0m:\n{err.decode()}')
    ssh.close()

if __name__ == '__main__':
    if len(sys.argv) < 3:
        print(f'Usage: {sys.argv[0]} ipfile commands')
        exit(1)

    if not os.path.exists(sys.argv[1]):
        print(f'No such file: {sys.argv[1]}')
        exit(2)

    ipfile = sys.argv[1]
    commands = ' '.join(sys.argv[2:])  # 拼接出要执行的命令
    passwd = getpass.getpass()

    with open(ipfile) as fobj:
        for line in fobj:
            ip = line.strip()  # 去除结尾的\n
            t = threading.Thread(target=rcmd, args=(ip, 22, 'root', passwd, commands))
            t.start()
            # rcmd(ip, 22, 'root', passwd, commands)
