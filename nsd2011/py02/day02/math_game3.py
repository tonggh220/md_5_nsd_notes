from random import randint, choice

def exam():
    '用于出题，用户作答'
    funcs = {'+': lambda x, y: x + y, '-': lambda x, y: x - y}
    # 随机生成两个数字
    nums = [randint(1, 100) for i in range(2)]
    nums.sort(reverse=True)  # 降序排列
    # 随机取出加减号
    op = choice('+-')
    # 计算出标准答案
    result = funcs[op](*nums)

    i = 0
    # 用户作答
    prompt = f'{nums[0]} {op} {nums[1]} = '
    while i < 3:
        try:
            answer = int(input(prompt))
        except:  # 裸except语句，可以捕获所有异常。不推荐
            print()  # 打印回车
            continue

        if answer == result:
            print('Very Good!!!')
            break
        print('Wrong Answer!!!')
        i += 1
    else:
        print('The Answer:\n', f'{prompt}{result}')

def main():
    '主程序代码逻辑'
    while 1:
        exam()
        try:
            yn = input('Continue(Y/n)? ').strip()[0]  # 取出第一个字符
        except (KeyboardInterrupt, EOFError):
            yn = 'n'
        except IndexError:
            continue

        if yn in 'nN':
            print('\nBye-bye')
            break

if __name__ == '__main__':
    main()
