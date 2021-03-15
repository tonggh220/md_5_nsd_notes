# 斐波那契数列

fib = [0, 1]
for i in range(8):
    fib.append(fib[-1] + fib[-2])

print(fib)
