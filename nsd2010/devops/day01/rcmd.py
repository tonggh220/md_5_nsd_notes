import paramiko

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
    rcmd('127.0.0.1', passwd='redhat', cmd='id root; id zhangsan')
