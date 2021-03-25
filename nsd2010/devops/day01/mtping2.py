import subprocess
import threading

class Ping:
    def __call__(self, host):
        result = subprocess.run(f'ping -c2 {host} &> /dev/null', shell=True)
        if result.returncode == 0:
            print(f'{host}:up')
        else:
            print(f'{host}:down')

if __name__ == '__main__':
    ips = (f'172.40.50.{i}' for i in range(1, 255))
    for ip in ips:
        t = threading.Thread(target=Ping(), args=(ip,))
        t.start()
