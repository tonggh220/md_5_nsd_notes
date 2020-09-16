from random import randint, choice

def add(x, y):
    return x + y

def sub(x, y):
    return x - y

def exam():
    "用于出题，让用户作答"
    funcs = {'+': add, '-': sub}
    # 随机选择两个数字
    nums = [randint(1, 100) for i in range(2)]
    nums.sort(reverse=True)  # 降序排列

    # 随机选择加减法
    op = choice('+-')

    # 计算出标准答案
    result = funcs[op](*nums)

    # 用户作答
    prompt = '%s %s %s = ' % (nums[0], op, nums[1])
    i = 0
    while i < 3:
        try:
            answer = int(input(prompt))
        except:  # 不指定异常，可以捕获所有异常。不推荐
            print()
            continue

        if answer == result:
            print('不错哟！')
            break
        print('不对呦！')
        i += 1
    else:
        print('正确答案是:\n%s%s' % (prompt, result))

def main():
    "主程序代码逻辑"
    while 1:
        exam()
        # 去除得到的字符串两端的空格后，取第一个字符
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
