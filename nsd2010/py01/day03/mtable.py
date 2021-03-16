# 打印3个hello
# for i in range(1, 4):
#     print('hello')

# 在一行内打印3个hello，print默认在打印结束时再打印一个\n，可以通过end=进行修改
# for i in range(1, 4):
#     print('hello', end='\t')

# 在一行内打印3个hello，然后打印回车
# for i in range(1, 4):
#     print('hello', end='\t')
# print()  # print默认在打印结束时再打印一个\n

# 将上面的代码当成一个整体，执行3遍
# for i in range(1, 4):
#     for j in range(1, 4):
#         print('hello', end='\t')
#     print()

# 第1行打印1个hello，第2行2个，第3行3个，第i行i个
# for i in range(1, 4):
#     for j in range(1, i + 1):
#         print('hello', end='\t')
#     print()

for i in range(1, 10):
    for j in range(1, i + 1):
        print(f'{j}x{i}={i*j}', end='\t')
    print()
