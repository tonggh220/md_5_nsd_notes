# 定义用于保存结果的变量
fib = [0, 1]

# 循环8次，每次将列表的最后两项相加，结果追加到列表中
for i in range(8):
    fib.append(fib[-1] + fib[-2])

print(fib)
