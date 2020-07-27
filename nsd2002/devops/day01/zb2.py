import os
import time

print('starting...')
ret_val = os.fork()

if ret_val:
    print('parent')
    result = os.waitpid(-1, 0)  # 挂起父进程，直到子进程结束并处理后才继续
    print(result)  # 返回值为(子进程pid, 0)
    time.sleep(20)
    print('parent done')
else:
    print('child')
    time.sleep(20)
    print('child done')
