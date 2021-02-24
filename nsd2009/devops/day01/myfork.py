import os

# print('starting...')
# os.fork()
# print('hello world!')
################
# print('starting...')
# rc = os.fork()
#
# if rc:
#     print('in parent')
# else:
#     print('in child')
#
# print('hello world!')
################

print('starting...')
for i in range(3):
    rc = os.fork()
    if not rc:
        print('Hello World!')
        exit()





