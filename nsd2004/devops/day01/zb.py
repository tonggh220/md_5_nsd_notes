import time
import os

print('starting...')
ret_val = os.fork()
if ret_val:
    print('in parent')
    time.sleep(60)
    print('parent done')
else:
    print('in child')
    time.sleep(30)
    print('child done')

# watch -n1 ps a
