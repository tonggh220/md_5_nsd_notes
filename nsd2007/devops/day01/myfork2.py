import os

print('starting...')

for i in range(3):
    rv = os.fork()
    if rv == 0:
        print('Hello World!')
        exit()

