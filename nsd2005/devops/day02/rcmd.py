#!/bin/python3

import threading
import sys
import os
import getpass
import paramiko

def rcmd(host, port=22, user='root', passwd=None, cmd=None):
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh.connect(host, port=port, username=user, password=passwd)
    stdin, stdout, stderr = ssh.exec_command(cmd)
    out = stdout.read()
    err = stderr.read()
    if out:
        print('[%s] \033[32;1mOUT\033[0m:\n%s' % (host, out.decode()))
    if err:
        print('[%s] \033[31;1mERROR\033[0m:\n%s' % (host, err.decode()))
    ssh.close()

if __name__ == '__main__':
    if len(sys.argv) < 3:
        print('Usage: %s ipfile commands' % sys.argv[0])
        exit(1)
    if not os.path.isfile(sys.argv[1]):
        print('No such file:', sys.argv[1])
        exit(2)

    ipfile = sys.argv[1]
    user = 'root'
    cmds = ' '.join(sys.argv[2:])  # 将命令拼接成字符串
    passwd = getpass.getpass()
    with open(ipfile) as fobj:
        for line in fobj:
            ip = line.strip()  # 去除行尾的\n
            t = threading.Thread(target=rcmd, args=(ip, 22, 'root', passwd, cmds))
            t.start()
            # rcmd('127.0.0.1', 22, 'root', 'redhat', 'sleep 3; id root')
