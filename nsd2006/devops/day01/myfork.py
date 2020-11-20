# import os
#
# print('starting...')
# os.fork()
# print('Hello World!')

# import os
#
# print('starting...')
#
# ret_val = os.fork()
# if ret_val:
#     print('in parent')
# else:
#     print('in child')
#
# print('Hello World!')


import os

print('starting...')

for i in range(3):
    ret_val = os.fork()
    if not ret_val:
        print('Hello World!')
        exit()

