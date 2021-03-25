import os

# print('starting...')
# os.fork()
# print('hello world!')
##################################
print('starting...')
ret_val = os.fork()

if ret_val:    # 如果是父进程，值非0，为真；如果是子进程，值是0，为假
    print('from parent')
else:
    print('from child')

print('hello world!')


