# import os
# import time
#
# print('starting...')
# ret_val = os.fork()
# if ret_val:
#     print('in parent')
#     time.sleep(15)
#     result = os.waitpid(-1, 0)
#     time.sleep(15)
# else:
#     print('in child')
#     time.sleep(10)

import os
import time

print('starting...')
ret_val = os.fork()
if ret_val:
    print('in parent')
    result = os.waitpid(-1, 0)  # 挂起父进程
    print(result)  # 僵尸进程处理掉后，返回值是(子进程的pid, 0)
    time.sleep(15)
else:
    print('in child')
    time.sleep(10)
