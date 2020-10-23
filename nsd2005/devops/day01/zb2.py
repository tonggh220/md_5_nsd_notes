import os
import time

print('starting...')
ret_val = os.fork()
if ret_val:
    print('in parent')
    result = os.waitpid(-1, 0)
    print(result)
    time.sleep(15)
    print('parent done')
else:
    print('in child')
    time.sleep(15)
    print('child done')

# watch -n1 ps a

