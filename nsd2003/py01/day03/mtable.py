# 打印3个hello
# for j in range(1, 4):
#     print('hello')  # print默认在结尾打印\n

# 打印3个hello，在一行内打印
# for j in range(1, 4):
#     print('hello', end='\t')  # 自定义print结尾打印\t
# print()  # 打印一行hello后，打印\n

# 将上面的代码作为一个整体，执行3遍
# for i in range(1, 4):
#     for j in range(1, 4):
#         print('hello', end='\t')
#     print()

# 第一行打印1个hello，第i行打印i个Hello
# for i in range(1, 4):
#     for j in range(1, i + 1):
#         print('hello', end='\t')
#     print()

for i in range(1, 10):
    for j in range(1, i + 1):
        print('%sx%s=%s' % (j, i, i * j), end='\t')
    print()
