import paramiko
import getpass
import sys
import threading
import os

def rcmd(host, port=22, user='root', passwd=None, cmd=None):
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh.connect(host, port=port, username=user, password=passwd)
    stdin, stdout, stderr = ssh.exec_command(cmd)
    out = stdout.read()
    err = stderr.read()
    if out:
        print(f'[{host}] \033[32;1mOUT\033[0m:\n{out.decode()}')
    if err:
        print(f'[{host}] \033[31;1mERROR\033[0m:\n{err.decode()}')

if __name__ == '__main__':
    # rcmd('127.0.0.1', passwd='redhat', cmd='id root; id zhangsan')
    if len(sys.argv) < 3:  # 命令加参数长度不能小于3
        print(f'Usage: {sys.argv[0]} ipfile commands')
        exit(1)
    if not os.path.isfile(sys.argv[1]):  # ip地址文件必须存在
        print(f'No such file: {sys.argv[1]}')
        exit(2)

    ipfile = sys.argv[1]
    cmd = ' '.join(sys.argv[2:])  # 拼接出命令
    passwd = getpass.getpass()
    with open(ipfile) as fobj:
        for line in fobj:
            ip = line.strip()  # 去除行尾的的\n
            t = threading.Thread(target=rcmd, args=(ip, 22, 'root', passwd, cmd))
            t.start()
            # rcmd(ip, 22, 'root', passwd, cmd)
