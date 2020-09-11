def mk_fib(n=10):
    fib = [0, 1]

    for i in range(n - 2):
        fib.append(fib[-1] + fib[-2])

    return fib

l1 = mk_fib(20)
print(l1)
l2 = mk_fib()
print(l2)
