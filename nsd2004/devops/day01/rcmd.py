import paramiko

def rcmd(host, port=22, user='root', passwd=None, cmds=None):
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh.connect(host, port, user, passwd)
    stdin, stdout, stderr = ssh.exec_command(cmds)
    out = stdout.read()
    err = stderr.read()
    ssh.close()
    if out:
        print('[%s] \033[32;1mOUT\033[0m:\n%s' % (host, out.decode()))
    if err:
        print('[%s] \033[31;1mERROR\033[0m:\n%s' % (host, err.decode()))

if __name__ == '__main__':
    rcmd('127.0.0.1', 22, 'root', 'redhat', 'id root; id zhangsan')
