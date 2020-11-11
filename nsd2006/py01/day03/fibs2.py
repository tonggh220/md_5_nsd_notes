def mk_fib(n):
    fib = [0, 1]

    for i in range(n - 2):
        fib.append(fib[-1] + fib[-2])

    return fib

l1 = mk_fib(10)
a = int(input("长度: "))
l2 = mk_fib(a)
print(l1)
print(l2)
