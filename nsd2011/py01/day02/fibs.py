# 首先定义用于保存结果的变量
fib = [0, 1]

# 向列表中加入8项数字
for i in range(8):
    fib.append(fib[-1] + fib[-2])

print(fib)
