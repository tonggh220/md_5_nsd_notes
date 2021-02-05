# 打印3个hello
# for j in range(1, 4):
#     print('hello')

# 在一行打印3个hello
# for j in range(1, 4):
#     print('hello', end='\t')  # print函数默认使用end='\n'在结尾打印回车，可以改变它
# print()  # 默认打印回车

# 把打印一行hello再打印一个回车，作为整体，执行3遍
# for i in range(1, 4):
#     for j in range(1, 4):
#         print('hello', end='\t')  # print函数默认使用end='\n'在结尾打印回车，可以改变它
#     print()  # 默认打印回车

# 第几行就打印几个hello
# for i in range(1, 10):
#     for j in range(1, i + 1):
#         print('hello', end='\t')  # print函数默认使用end='\n'在结尾打印回车，可以改变它
#     print()  # 默认打印回车

for i in range(1, 10):
    for j in range(1, i + 1):
        print('%sx%s=%s' % (j, i, i * j), end='\t')  # print函数默认使用end='\n'在结尾打印回车，可以改变它
    print()  # 默认打印回车
