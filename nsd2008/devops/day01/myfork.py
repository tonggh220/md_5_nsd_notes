import os

print('starting...')
ret_val = os.fork()
if ret_val:
    print('in parent')
else:
    print('in child')

print('Hello World!')
