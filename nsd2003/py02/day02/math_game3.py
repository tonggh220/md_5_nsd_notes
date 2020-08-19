from random import randint, choice

def exam():
    '用于出题，让用户作答'
    funcs = {'+': lambda x, y: x + y, '-': lambda x, y: x - y}
    # 随机生成两个100以内的数字
    nums = [randint(1, 100) for i in range(2)]
    nums.sort(reverse=True)  # 降序排列
    # 随机选择加法或是减法
    op = choice('+-')

    # 算出标准答案
    result = funcs[op](*nums)

    # 用户作答
    prompt = '%s %s %s = ' % (nums[0], op, nums[1])
    n = 0
    while n < 3:
        try:
            answer = int(input(prompt))
        except:  # 不指定具体的异常，可以捕获所有异常。不推荐
            print()
            continue

        if answer == result:
            print('你真棒！！！')
            break
        print('不对哟！！！')
        n += 1
    else:
        print('%s%s' % (prompt, result))

def main():
    while 1:
        exam()
        # 去除用户输入的额外空格，并取第一个字符
        try:
            yn = input('Continue(y/n)? ').strip()[0]
        except IndexError:
            continue
        except (KeyboardInterrupt, EOFError):
            yn = 'n'

        if yn in 'nN':
            print('\nBye-bye')
            break

if __name__ == '__main__':
    main()
