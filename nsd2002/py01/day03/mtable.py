# 打印3个hello，print默认在结尾打印一个\n
# for i in range(1, 4):
#     print('hello')

# 打印3个hello，print接受一个名为end的参数，可以指定使用什么替换\n
# for i in range(1, 4):
#     print('hello', end='\t')
# print()   # 打印回车

# 将上面的内容作为一个主体，再运行3遍
# for a in range(1, 4):
#     for i in range(1, 4):
#         print('hello', end='\t')
#     print()   # 打印回车

# 要求第一行打印1个hello，第二行2个，第3行3个，第a行a个
# for a in range(1, 4):
#     for i in range(1, a + 1):
#         print('hello', end='\t')
#     print()   # 打印回车

for i in range(1, 10):
    for j in range(1, i + 1):
        print('%s x %s = %s' % (j, i, i * j), end='\t')
    print()
