import os

# print('starting...')
# os.fork()
# print('Hello World!')

# print('starting...')
#
# rc = os.fork()  # os.fork()的返回值是整数数字
# if rc:  # 如果是父进程，值非0，为真；如果是子进程，值是0，为假
#     print('Hello from parent')
# else:
#     print('Hello from child')
#
# print('Hello World!')


print('starting...')

for i in range(3):
    rc = os.fork()
    if not rc:
        print('Hello World!')
        exit()
