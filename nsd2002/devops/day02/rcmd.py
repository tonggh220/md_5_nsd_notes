import paramiko
import sys
import os
import getpass
import threading

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
    # 判断命令行的长度，如果小于3则退出
    if len(sys.argv) < 3:
        print('Usage: %s ipfile commands' % sys.argv[0])
        exit(1)
    ipfile = sys.argv[1]
    cmds = ' '.join(sys.argv[2:])  # 将列表中命令部分拼接为字符串
    # 判断主机地址文件是否存在，不存在则退出
    if not os.path.isfile(ipfile):
        print('No such file:', ipfile)
        exit(2)
    # 获取密码
    passwd = getpass.getpass()
    # 在文件中取出ip地址，在每个ip地址上执行指令
    with open(ipfile) as fobj:
        for line in fobj:
            ip = line.strip()  # 去除每行结尾的\n
            t = threading.Thread(target=rcmd, args=(ip, 22, 'root', passwd, cmds))
            t.start()
    # rcmd('192.168.1.136', passwd='redhat', cmds='id root; id zhangsan')
