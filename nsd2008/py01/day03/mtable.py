# 打印3个hello
# for j in range(1, 4):
#     print('hello')

# print默认在结尾打印回车\n，通过end参数可进行修改
# for j in range(1, 4):
#     print('hello', end='\t')

# 为了使得命令行提示符能够在新一行出现，再打印一个回车\n
# for j in range(1, 4):
#     print('hello', end='\t')
# print()

# 将上面的代码作为一个整体，执行3遍
# for i in range(1, 4):
#     for j in range(1, 4):
#         print('hello', end='\t')
#     print()

# 将上面代码改为第1行1个hello，第2行2个，第i行i个
# for i in range(1, 10):
#     for j in range(1, i + 1):
#         print('hello', end='\t')
#     print()

# 实现99乘法表
for i in range(1, 10):
    for j in range(1, i + 1):
        print('%sx%s=%s' % (j, i, i * j), end='\t')
    print()
