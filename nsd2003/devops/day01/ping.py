import subprocess

def ping(host):
    result = subprocess.run('ping -c2 %s &> /dev/null' % host, shell=True)
    if result.returncode == 0:
        print('%s:up' % host)
    else:
        print('%s:down' % host)

if __name__ == '__main__':
    ips = ('192.168.1.%s' % i for i in range(1, 255))
    for ip in ips:
        ping(ip)
