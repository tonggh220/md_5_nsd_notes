# 声明用于保存结果的变量
fib = [0, 1]

for i in range(8):
    fib.append(fib[-1] + fib[-2])

print(fib)
