import paramiko
import sys
import threading
import getpass
import os

def rcmd(host, user, passwd, port=22, cmds=None):
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh.connect(host, port=port, username=user, password=passwd)
    stdin, stdout, stderr = ssh.exec_command(cmds)
    out = stdout.read()
    err = stderr.read()
    if out:
        print('[%s] \033[32;1mOUT\033[0m:\n%s' % (host, out.decode()))
    if err:
        print('[%s] \033[31;1mERROR\033[0m:\n%s' % (host, err.decode()))
    ssh.close()

if __name__ == '__main__':
    # rcmd('127.0.0.1', 'root', 'redhat', cmds='id root; id zhangsan')
    if len(sys.argv) < 3:
        print('Usage: %s ipfile commands' % sys.argv[0])
        exit(1)

    if not os.path.isfile(sys.argv[1]):
        print('No such file:', sys.argv[1])
        exit(2)

    ipfile = sys.argv[1]
    cmds = ' '.join(sys.argv[2:])
    passwd = getpass.getpass()
    with open(ipfile) as fobj:
        for line in fobj:
            ip = line.strip()
            # rcmd(ip, 'root', 'redhat', 22, cmds)
            t = threading.Thread(target=rcmd, args=(ip, 'root', passwd, 22, cmds))
            t.start()

# vim servers.txt
# 192.168.1.154
# 127.0.0.1
# python3 rcmd.py servers.txt id root
