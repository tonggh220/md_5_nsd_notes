def mk_fib():
    result = [0, 1]

    l = int(input('长度: '))

    for i in range(l - 2):
        result.append(result[-1] + result[-2])

    print(result)

mk_fib()  # 调用函数
