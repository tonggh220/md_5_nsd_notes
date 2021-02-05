def mk_fib():
    fib = [0, 1]

    n = int(input("长度: "))
    for i in range(n - 2):
        fib.append(fib[-1] + fib[-2])

    return fib  # 返回fib代表的列表

a = mk_fib()  # 调用mk_fib函数后，得到的值赋值给变量a
print(a)
