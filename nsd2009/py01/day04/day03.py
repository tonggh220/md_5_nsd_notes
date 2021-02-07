# users = ['tom', 'jerry', 'jack', 'rose']

# for i in [0, 1, 2, 3]:
#     print(i, users[i])

# for i in range(4):
#     print(i, users[i])

# for i in range(len(users)):
#     print(i, users[i])

users = ['tom', 'jerry', 'jack', 'rose']
# >>> list(enumerate(users))
# enumerate(users)是由元组构成的，所以data是元组
# for data in enumerate(users):
#     print(data)

for i, user in enumerate(users):
    print(i, user)

