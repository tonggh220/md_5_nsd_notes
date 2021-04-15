# 首先定义用于保存结果的变量
fib = [0, 1]

n = int(input('长度: '))
# 向列表中加入n项数字
for i in range(n - 2):
    fib.append(fib[-1] + fib[-2])

print(fib)
