def mk_fib(n):
    fib = [0, 1]

    for i in range(n - 2):
        fib.append(fib[-1] + fib[-2])

    return fib


num = int(input('长度: '))
l1 = mk_fib(num)
print(l1)
l2 = mk_fib(10)
print(l2)
