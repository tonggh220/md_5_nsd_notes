import os

print('starting...')

for i in range(3):
    ret_val = os.fork()
    if not ret_val:
        print('hello world!')
        exit()
