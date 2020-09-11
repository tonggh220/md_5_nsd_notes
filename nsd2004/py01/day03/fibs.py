def mk_fib():
    fib = [0, 1]

    n = int(input("数列长度: "))

    for i in range(n - 2):
        fib.append(fib[-1] + fib[-2])

    print(fib)

mk_fib()
mk_fib()
