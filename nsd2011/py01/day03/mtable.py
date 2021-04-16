# for j in range(3):
#     print('hello')  # print函数默认在结尾打印\n

# 打印一行hello
# for j in range(1, 4):
#     print('hello', end='\t')  # 修改print默认行为，在结尾打印\t

# 打印一行hello后，再打印回车
# for j in range(1, 4):
#     print('hello', end='\t')
# print()   # 打印回车\n

# 将上面打印3行hello的代码作为一个整体，运行3遍
# for i in range(3):
#     for j in range(1, 4):
#         print('hello', end='\t')
#     print()

for i in range(1, 4):
    for j in range(1, i + 1):
        print('hello', end='\t')
    print()

# for i in range(1, 10):
#     for j in range(1, i + 1):
#         print(f'{j}x{i}={i * j}', end='\t')
#     print()
