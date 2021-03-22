from random import randint, choice

def exam():
    '用于出题，用户作答'
    funcs = {'+': lambda x, y: x + y, '-': lambda x, y: x - y}
    # 随机生成两个整数
    nums = [randint(1, 100) for i in range(2)]
    nums.sort(reverse=True)  # 降序排列
    # nums.reverse()

    # 随机选择加减法
    op = choice('+-')
    # 计算出标准答案
    result = funcs[op](*nums)

    # 用户作答，判断正误
    prompt = f'{nums[0]} {op} {nums[1]} = '
    n = 0

    while n < 3:
        try:
            answer = int(input(prompt))
        except:  # 裸except可以捕获所有异常，不推荐
            print()
            continue

        if answer == result:
            print('你真棒!!!')
            break
        print('不对哟!!!')
        n += 1
    else:
        print(f'正确答案是:\n{prompt}{result}')

def main():
    '主程序代码逻辑'
    while 1:
        exam()
        try:
            yn = input('Continue(Y/n)? ').strip()[0]  # 取出用户输入的第一个非空字符
        except IndexError:
            continue
        except (KeyboardInterrupt, EOFError):
            yn = 'n'

        if yn in 'nN':
            print('\nBye-bye')
            break

if __name__ == '__main__':
    main()
