from random import randint, choice

def exam():
    "用于出题，用户作答"
    funcs = {'+': lambda x, y: x + y, '-': lambda x, y: x - y}
    # 随机生成两个数字，并降序排列
    nums = [randint(1, 100) for i in range(2)]
    nums.sort(reverse=True)
    # nums.reverse()
    # 随机选择加减法
    op = choice('+-')
    # 计算出标准答案
    result = funcs[op](*nums)

    prompt = '%s %s %s = ' % (nums[0], op, nums[1])
    i = 0
    while i < 3:
        # 用户作答，判断对错
        try:
            answer = int(input(prompt))
        except:  # 不指定具体异常，可以捕获所有异常。不推荐
            print()
            continue

        if answer == result:
            print('Very Good!!!')
            break
        print('Wrong Answer!!!')
        i += 1
    else:
        print('The Answer: %s%s' % (prompt, result))

def main():
    "用于主程序代码逻辑"
    while 1:
        exam()
        # 去除字符串两端空格后，取出第一个字符
        try:
            yn = input("Continue(y/n)? ").strip()[0]
        except (KeyboardInterrupt, EOFError):
            yn = 'n'
        except IndexError:
            continue

        if yn in 'nN':
            print('\nBye-bye')
            break

if __name__ == '__main__':
    main()
