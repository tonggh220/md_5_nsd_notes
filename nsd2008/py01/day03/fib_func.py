def mk_fib(n):  # 函数需要处理的数据用参数传递
    fib = [0, 1]

    for i in range(n - 2):
        fib.append(fib[-1] + fib[-2])

    return fib  # 返回fib变量代表的列表，不是把fib变量返回

length = int(input("长度: "))
result1 = mk_fib(length)
print(result1)
result2 = mk_fib(8)
print(result2)

