import os

# print('starting...')
# os.fork()
# print('Hello World!')


# print('starting...')
# ret_val = os.fork()
# if ret_val:  # 如果值非0，意味着是父进程
#     print('父进程')
# else:
#     print('子进程')
# print('Hello World!')

for i in range(3):
    ret_val = os.fork()
    if not ret_val:  # 如果是子进程则打印
        print('Hello World!')
        exit()


