def mk_fib():
    result = [0, 1]

    l = int(input('长度: '))
    for i in range(l - 2):
        result.append(result[-1] + result[-2])

    return result

l1 = mk_fib()  # 调用函数
print(l1)
l2 = [i + 100 for i in l1]
print(l2)
