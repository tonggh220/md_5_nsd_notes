import os
import time

ret_val = os.fork()
if ret_val:
    print('in parent')
    result = os.waitpid(-1, 0)  # 挂起父进程，直到处理完僵尸进程
    print(result)
    time.sleep(15)
else:
    print('in child')
    time.sleep(15)
