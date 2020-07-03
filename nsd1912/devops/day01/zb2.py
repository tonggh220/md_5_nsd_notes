import os
import time

print('starting...')

ret_val = os.fork()
if ret_val:
    print('Hello From Parent')
    # result = os.waitpid(-1, 0)  # 挂起父进程
    # print(result)   # (子进程pid, 0)
    result = os.waitpid(-1, 1)  # 不挂起父进程
    print(result)   # (0, 0)
    time.sleep(60)
    print('Parent Done')
else:
    print('Hello From Child')
    time.sleep(15)
    print('Child Done')

# watch -n1 ps a
