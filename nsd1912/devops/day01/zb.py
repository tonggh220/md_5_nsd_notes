import os
import time

print('starting...')

ret_val = os.fork()
if ret_val:
    print('Hello From Parent')
    time.sleep(60)
    print('Parent Done')
else:
    print('Hello From Child')
    time.sleep(15)
    print('Child Done')

# watch -n1 ps a
