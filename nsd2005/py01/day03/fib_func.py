def mk_fib(n=10):
    fib = [0, 1]

    for i in range(n - 2):
        fib.append(fib[-1] + fib[-2])

    return fib

a = mk_fib()
print(a)
n = int(input("长度: "))
b = mk_fib(n)
print(b)
