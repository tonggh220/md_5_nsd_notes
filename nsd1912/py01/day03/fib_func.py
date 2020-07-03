def mk_fib(n):
    fib = [0, 1]

    for i in range(n - 2):
        fib.append(fib[-1] + fib[-2])

    return fib

l1 = mk_fib(10)
print(l1)

for i in [5, 8, 10, 12, 20]:
    print(mk_fib(i))

n = int(input('长度: '))
print(mk_fib(n))
