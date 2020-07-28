import paramiko

def rcmd(host, port=22, user='root', passwd=None, cmds=None):
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh.connect(hostname=host, port=port, username=user, password=passwd)
    stdin, stdout, stderr = ssh.exec_command(cmds)
    out = stdout.read()
    err = stderr.read()
    if out:  # 如果out非空
        print('[\033[35;1m%s\033[0m]\033[32;1mOUT\033[0m:\n%s' % (host, out.decode()))
    if err:  # 如果err非空
        print('[\033[35;1m%s\033[0m]\033[31;1mERROR\033[0m:\n%s' % (host, err.decode()))
    ssh.close()

if __name__ == '__main__':
    rcmd('192.168.1.136', passwd='redhat', cmds='id root; id zhangsan')
