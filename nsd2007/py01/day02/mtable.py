# for j in range(1, 4):   # [1, 2, 3]
#     print('Hello', end='\t')
# print()

# for i in range(1, 4):
#     for j in range(1, 4):
#         print('Hello', end='\t')
#     print()

# for i in range(1, 10):
#     for j in range(1, i + 1):
#         print('Hello', end='\t')
#     print()

# for i in range(1, 10):
#     for j in range(1, i + 1):
#         print('%sx%s=%s' % (j, i, i * j), end='\t')
#     print()

l1 = [
    ['zhangsan', 'lisi', 'wangwu', 'zhaoliu'],
    [20, 22, 25, 23]
]

# for mylist in l1:
#     print(mylist)

for mylist in l1:
    for data in mylist:
        print(data)
