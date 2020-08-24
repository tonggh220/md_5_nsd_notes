import os
import time

print('starting...')
ret_val = os.fork()
if ret_val:
    print('parent')
    result = os.waitpid(-1, 1)  # 不挂起父进程,如果此时子进程是僵尸进程则处理掉，否则不管
    print(result)  # (0, 0)
    time.sleep(30)
    print('parent done')
else:
    print('child')
    time.sleep(15)
    print('child done')

