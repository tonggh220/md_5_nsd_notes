import os
import time

print('starting...')
ret_val = os.fork()

if ret_val:
    print('parent')
    time.sleep(60)
    print('parent done')
else:
    print('child')
    time.sleep(20)
    print('child done')
