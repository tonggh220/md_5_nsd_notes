import subprocess
import threading

class Ping:
    def __init__(self, host):
        self.host = host

    def __call__(self):
        result = subprocess.run(f'ping -c2 {self.host} &> /dev/null', shell=True)
        if result.returncode == 0:
            print(f'{self.host}:up')
        else:
            print(f'{self.host}:down')

if __name__ == '__main__':
    ips = (f'172.40.50.{i}' for i in range(1, 255))
    for ip in ips:
        t = threading.Thread(target=Ping(ip))
        t.start()
