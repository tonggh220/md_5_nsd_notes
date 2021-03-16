def mk_fib():
    fib = [0, 1]
    l = int(input("长度: "))

    for i in range(l - 2):
        fib.append(fib[-1] + fib[-2])

    return fib

l1 = mk_fib()
print(l1)
l2 = [100 + i for i in l1]
print(l2)
