def mk_fib(l):
    result = [0, 1]

    for i in range(l - 2):
        result.append(result[-1] + result[-2])

    return result

l1 = mk_fib(10)  # 调用函数
print(l1)
n = int(input('长度: '))
l2 = mk_fib(n)
print(l2)
