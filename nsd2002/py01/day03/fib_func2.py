def mk_fib(n):
    fib = [0, 1]

    for i in range(n - 2):
        fib.append(fib[-1] + fib[-2])

    return fib

r1 = mk_fib(10)
print(r1)
a = int(input("长度: "))
r2 = mk_fib(a)
print(r2)
