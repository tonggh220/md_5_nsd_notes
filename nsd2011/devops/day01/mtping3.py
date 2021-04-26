import subprocess
import threading

class Ping:
    def __init__(self, host):
        self.host = host

    def __call__(self):
        # 实例像函数一样调用时，调用此方法
        result = subprocess.run(
            f'ping -c2 {self.host} &> /dev/null', shell=True
        )
        if result.returncode == 0:
            print(f'{self.host}:up')
        else:
            print(f'{self.host}:down')

if __name__ == '__main__':
    ips = (f'172.40.0.{i}' for i in range(1, 255))
    for ip in ips:
        # 创建Ping的实例
        t = threading.Thread(target=Ping(ip))
        t.start()  # 调用target()
