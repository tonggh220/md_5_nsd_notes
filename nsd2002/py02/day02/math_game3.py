from random import randint, choice

def exam():
    "出题，用户作答"
    funcs = {'+': lambda x, y: x + y, '-': lambda x, y: x - y}
    # 随机生成2个数字
    nums = [randint(1, 100) for i in range(2)]
    nums.sort(reverse=True)  # 降序排列

    # 随机选择加减法
    op = choice('+-')

    # 计算出标准答案
    result = funcs[op](*nums)

    # 用户作答
    prompt = '%s %s %s = ' % (nums[0], op, nums[1])
    n = 0
    while n < 3:
        try:
            answer = int(input(prompt))
        except:  # 不写明异常，可以捕获所有异常，不推荐
            print()
            continue

        if answer == result:
            print('不错哟!!!')
            break
        print('不对哟!!!')
        n += 1
    else:
        print('Answer: %s%s' % (prompt, result))

def main():
    "程序的代码逻辑"
    while 1:
        exam()
        # 获取用户输入，去除两端空格再取出第一个字符
        try:
            yn = input('Continue(y/n)? ').strip()[0]
        except IndexError:
            continue
        except (KeyboardInterrupt, EOFError):
            yn = 'n'

        if yn in 'Nn':
            print('\nBye-bye')
            break

if __name__ == '__main__':
    main()
