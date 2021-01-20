import os
import time

ret_val = os.fork()
if ret_val:
    print('in parent')
    time.sleep(60)
else:
    print('in child')
    time.sleep(15)
