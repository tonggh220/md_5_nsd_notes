# 打印3行hello
# for j in range(1, 4):
#     print('Hello')

# print默认在结尾打印回车，可以能过end=改变
# for j in range(1, 4):
#     print('Hello', end='\t')
# print()  # 默认结尾打印回车

# 把上述代码作为一个整体，再执行3遍
# for i in range(1, 4):
#     for j in range(1, 4):
#         print('Hello', end='\t')
#     print()  # 默认结尾打印回车

# 第1行打印1个hello，第2行2个，第3行3个，第i行i个
for i in range(1, 4):
    for j in range(1, i + 1):
        print('Hello', end='\t')
    print()  # 默认结尾打印回车
