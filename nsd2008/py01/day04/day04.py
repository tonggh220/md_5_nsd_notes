users = ['tom', 'jerry', 'jack', 'rose']
# enumerate内部是由一个个元组构成的，元组第1项是下标，第2项是下标对应的值
# l1 = list(enumerate(users))
# print(l1)

# 取出enumerate内部的元组赋值给data
# for data in enumerate(users):
#     print(data)

# 打印元组中的两项
# for data in enumerate(users):
#     print(data[0], data[1])

# 把元组中的两项分别赋值给i和name
for i, name in enumerate(users):
    print(i, name)

# for i in [0, 1, 2, 3]:
#     print(i, users[i])

# for i in range(4):
#     print(i, users[i])

# for i in range(len(users)):
#     print(i, users[i])

