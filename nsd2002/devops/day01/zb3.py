import os
import time

print('starting...')
ret_val = os.fork()

if ret_val:
    print('parent')
    result = os.waitpid(-1, 1)  # 不挂起父进程，如果子进程是僵尸进程则处理掉，否则什么也不做，继续向下执行
    print(result)  # 返回值为(0, 0)
    time.sleep(40)
    print('parent done')
else:
    print('child')
    time.sleep(20)
    print('child done')
