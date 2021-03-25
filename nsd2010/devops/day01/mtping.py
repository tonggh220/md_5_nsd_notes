import subprocess
import threading

def ping(host):
    result = subprocess.run(f'ping -c2 {host} &> /dev/null', shell=True)
    if result.returncode == 0:
        print(f'{host}:up')
    else:
        print(f'{host}:down')

if __name__ == '__main__':
    ips = (f'172.40.50.{i}' for i in range(1, 255))
    for ip in ips:
        t = threading.Thread(target=ping, args=(ip,))
        t.start()
