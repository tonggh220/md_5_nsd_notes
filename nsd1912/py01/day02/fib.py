fib = [0, 1]  # 定义用于保存最终结果的列表

n = int(input('长度: '))
for i in range(n - 2):
    fib.append(fib[-1] + fib[-2])

print(fib)
