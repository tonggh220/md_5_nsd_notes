import paramiko
import sys
import getpass
import threading
import os

def rcmd(host, port=22, user='root', passwd=None, cmds=None):
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh.connect(host, port=port, username=user, password=passwd)
    stdin, stdout, stderr = ssh.exec_command(cmds)
    out = stdout.read()
    err = stderr.read()
    if out:  # 如果out非空
        print('[%s] OUT:\n%s' % (host, out.decode()))
    if err:  # 如果err非空
        print('[%s] ERROR:\n%s' % (host, err.decode()))
    ssh.close()

if __name__ == '__main__':
    # rcmd('192.168.81.132', passwd='redhat', cmds='id root; id zhangsan')
    if len(sys.argv) != 3:
        print("Usage: %s ipfile 'commands'" % sys.argv[0])
        exit(1)
    if not os.path.isfile(sys.argv[1]):
        print('No such file:', sys.argv[1])
        exit(2)
    fname = sys.argv[1]
    commands = sys.argv[2]
    passwd = getpass.getpass()
    with open(fname) as fobj:
        for line in fobj:
            ip = line.strip()  # 去除行尾的\n
            # rcmd(ip, passwd=passwd, cmds=commands)
            # t = threading.Thread(target=rcmd, args=(ip, 22, 'root', passwd, commands))
            t = threading.Thread(target=rcmd, args=(ip,), kwargs={'passwd': passwd, 'cmds': commands})
            t.start()
