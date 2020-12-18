import os

# print('starting...')
# os.fork()
# print('Hello World!')

print('starting...')
# os.fork()的返回值是数字，在父子进程中不一样。在子进程中是0，父进程是非0值
ret_val = os.fork()

if ret_val:
    print('父进程')
else:
    print('子进程')

print('Hello World!')


