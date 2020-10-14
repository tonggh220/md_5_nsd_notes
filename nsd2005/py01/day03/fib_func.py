def mk_fib(n):
    fib = [0, 1]

    for i in range(n - 2):
        fib.append(fib[-1] + fib[-2])

    return fib

a = mk_fib(10)
print(a)
n = int(input("长度: "))
b = mk_fib(n)
print(b)
