import subprocess
import threading

class Ping:
    def __call__(self, host):
        # 实例像函数一样调用时，调用此方法
        result = subprocess.run(
            f'ping -c2 {host} &> /dev/null', shell=True
        )
        if result.returncode == 0:
            print(f'{host}:up')
        else:
            print(f'{host}:down')

if __name__ == '__main__':
    ips = (f'172.40.0.{i}' for i in range(1, 255))
    for ip in ips:
        # 创建Ping的实例
        t = threading.Thread(target=Ping(), args=(ip,))
        t.start()  # 调用target(*args)
