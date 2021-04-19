users = ['tom', 'jerry', 'zhangsan', 'lisi']

# for i in [0, 1, 2, 3]:
#     print(i, users[i])

# for i in range(4):
#     print(i, users[i])

# for i in range(len(users)):
#     print(i, users[i])

# for data in enumerate(users):
#     print(data)

# for i, user in enumerate(users):
#     print(i, user)

num = input('number: ')
for ch in num:
    if ch not in '0123456789':
        print('不全是数字')
        break
else:
    print('全是数字')

