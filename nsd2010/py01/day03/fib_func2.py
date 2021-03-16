def mk_fib(l):
    fib = [0, 1]

    for i in range(l - 2):
        fib.append(fib[-1] + fib[-2])

    return fib

l1 = mk_fib(10)
print(l1)
n = int(input('长度: '))
l2 = mk_fib(n)
print(l2)
