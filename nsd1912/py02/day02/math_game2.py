from random import randint, choice

def add(x, y):
    return x + y

def sub(x, y):
    return x - y

def exam():
    "用于出题，让用户作答"
    funcs = {'+': add, '-': sub}
    # 随机生成两个数字，降序排列
    nums = [randint(1, 100) for i in range(2)]
    nums.sort(reverse=True)
    # 随机取出加减法
    op = choice('+-')
    # 计算正确答案
    result = funcs[op](*nums)

    # 要求用户作答
    n = 0
    prompt = '%s %s %s = ' % (nums[0], op, nums[1])
    while n < 3:
        try:
            answer = int(input(prompt))
        except:  # 可以捕获所有异常，但是不推荐
            print()  # 打印回车
            continue

        if answer == result:
            print('不错哟!!!')
            break
        print('不对哟')
        n += 1
    else:
        print('%s%s' % (prompt, result))

def main():
    "主程序代码"
    while 1:
        exam()
        # 去除两端空格后，取第一个字符
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
