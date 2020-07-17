# 定义函数时，只是声明有这样的一个功能，函数体内的代码不执行
def mk_fib():
    fib = [0, 1]

    n = int(input("长度: "))
    for i in range(n - 2):
        fib.append(fib[-1] + fib[-2])

    print(fib)

mk_fib()  # 调用函数，就是将函数体内的代码执行一次
