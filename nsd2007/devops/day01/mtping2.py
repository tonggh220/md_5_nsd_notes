import subprocess
import threading

class Ping:
    def __call__(self, host):
        # 实例像函数一样调用时，就是执行__call__中的代码
        result = subprocess.run(
            'ping -c2 %s &> /dev/null' % host, shell=True
        )
        if result.returncode == 0:
            print('%s:up' % host)
        else:
            print('%s:down' % host)

if __name__ == '__main__':
    ips = ('172.40.91.%s' % i for i in range(1, 255))
    for ip in ips:
        t = threading.Thread(target=Ping(), args=(ip,))  # 创建Ping的实例
        t.start()   # 相当于执行target(*args)
