import os

# print('starting...')
# os.fork()
# print('Hello World!')

print('starting...')
ret_val = os.fork()
if ret_val:
    print('in parent')
else:
    print('in child')
print('Hello World!')
