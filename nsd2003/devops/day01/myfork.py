import os

# print('starting...')
# os.fork()
# print('Hello World!')

print('starting...')
ret_val = os.fork()  # 如果是父进程，值非0，为真；如果是子进程，值是0，为假
if ret_val:
    print('in parent')
else:
    print('in child')
print('Hello World!')



