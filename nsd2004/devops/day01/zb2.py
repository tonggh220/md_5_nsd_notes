import time
import os

print('starting...')
ret_val = os.fork()
if ret_val:
    print('in parent')
    result = os.waitpid(-1, 0)  # 挂起，直到处理掉子进程才向下执行
    print(result)   # (子进程pid, 0)
    time.sleep(20)
    print('parent done')
else:
    print('in child')
    time.sleep(30)
    print('child done')

# watch -n1 ps a
