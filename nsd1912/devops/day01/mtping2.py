import subprocess
import threading

class Ping:
    def __call__(self, host):
        result = subprocess.run('ping -c2 %s &> /dev/null' % host, shell=True)
        if result.returncode == 0:
            print('%s:up' % host)
        else:
            print('%s:down' % host)

if __name__ == '__main__':
    ips = ('192.168.81.%s' % i for i in range(1, 255))
    for ip in ips:
        t = threading.Thread(target=Ping(), args=(ip,))  # target是Ping的实例
        t.start()  # target(*args)  # 实例像函数一样调用时，执行__call__方法中的代码
