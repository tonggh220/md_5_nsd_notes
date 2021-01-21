import paramiko
import sys
import getpass
import threading
import os

def rcmd(host, port=22, user='root', passwd=None, cmd=None):
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh.connect(host, port, user, passwd)
    stdin, stdout, stderr = ssh.exec_command(cmd)
    out = stdout.read()
    err = stderr.read()
    if out:  # 如果out非空，则输出
        print("[%s]\033[32;1mOUT\033[0m:\n%s" % (host, out.decode()))

    if err:  # 如果err非空，则输出
        print("[%s]\033[31;1mERROR\033[0m:\n%s" % (host, err.decode()))

    ssh.close()

if __name__ == '__main__':
    if len(sys.argv) < 2:
        print('Usage: %s ipfile command' % sys.argv[0])
        exit(1)

    if not os.path.isfile(sys.argv[1]):
        print('No such file:', sys.argv[1])
        exit(2)

    ipfile = sys.argv[1]
    cmd = ' '.join(sys.argv[2:])
    passwd = getpass.getpass()
    with open(ipfile) as fobj:
        for line in fobj:
            ip = line.strip()  # 移除行尾的\n
            # rcmd(ip, 22, 'root', passwd, cmd)
            t = threading.Thread(
                target=rcmd,
                args=(ip, 22, 'root', passwd, cmd)
            )
            t.start()
