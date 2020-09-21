import time
import os

print('starting...')
ret_val = os.fork()
if ret_val:
    print('in parent')
    result = os.waitpid(-1, 1)  # 不挂起，子进程没有变成僵尸进程，无法处理，继续向下运行
    print(result)   # (0, 0)
    time.sleep(60)
    print('parent done')
else:
    print('in child')
    time.sleep(30)
    print('child done')

# watch -n1 ps a
