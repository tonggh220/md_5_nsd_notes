def mk_fib(n):
    fib = [0, 1]

    for i in range(n - 2):
        fib.append(fib[-1] + fib[-2])

    return fib

n1 = int(input("长度: "))
l1 = mk_fib(n1)
l2 = mk_fib(8)
print(l1)
print(l2)
