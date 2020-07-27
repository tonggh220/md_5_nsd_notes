import os

# print('starting...')
# os.fork()
# print('Hello World!')


# print('starting...')
# ret_val = os.fork()
# if ret_val:  # 如果是父进程，值非0，为真；如果是子进程，值是0，为假
#     print('parent')
# else:
#     print('child')
#
# print('Hello World!')

for i in range(3):
    ret_val = os.fork()
    if not ret_val:
        print('Hello World!')
        exit(0)









