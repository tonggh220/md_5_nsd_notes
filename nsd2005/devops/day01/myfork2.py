import os

print('starting...')

for i in range(3):
    ret_val = os.fork()
    if not ret_val:
        print('Hello World')
        exit()  # 子进程遇到exit将会彻底结束
