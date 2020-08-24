import os
import time

print('starting...')
ret_val = os.fork()
if ret_val:
    print('parent')
    result = os.waitpid(-1, 0)  # 挂起父进程,等待子进程结束，以便回收掉它
    print(result)  # (子进程pid, 0)
    time.sleep(30)
    print('parent done')
else:
    print('child')
    time.sleep(15)
    print('child done')

