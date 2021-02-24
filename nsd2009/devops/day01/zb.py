import os
import time

print('starting...')

rc = os.fork()
if rc:
    print('in parent')
    time.sleep(30)
    result = os.waitpid(-1, 0)  # 处理僵尸进程
    print(result)   # result: (僵尸进程id, 0)
    time.sleep(10)
    print('parent done')
else:
    print('in child')
    time.sleep(15)
    print('child done')


