from random import randint, choice

def exam():
    "出题，用户作答"
    funcs = {'+': lambda x, y: x + y, '-': lambda x, y: x - y}
    # 随机选择2个整数并降序排列
    nums = [randint(1, 100) for i in range(2)]
    nums.sort(reverse=True)  # 降序排列
    # 随机选择加减法
    op = choice('+-')
    # 计算出标准答案
    result = funcs[op](*nums)

    # 用户作答，判断正误
    prompt = '%s %s %s = ' % (nums[0], op, nums[1])  # 拼接出算式
    n = 0
    while n < 3:
        try:
            answer = int(input(prompt))
        except:  # 不指定异常，可以捕获所有异常。不推荐
            print()  # 打印回车
            continue

        if answer == result:
            print('Very Good!!!')
            break
        print('Wrong Answer!!!!')
        n += 1
    else:  # 如果用户3次全错才给出正确答案
        print('The Answer:\n%s%s' % (prompt, result))

def main():
    "主程序代码逻辑"
    while 1:
        exam()
        try:
            yn = input("Continue(y/n)? ").strip()[0]  # 取用户输入的第一个非空格字符
        except (KeyboardInterrupt, EOFError):
            yn = 'n'
        except IndexError:
            continue

        if yn in 'nN':
            print('\nBye-bye')
            break

if __name__ == '__main__':
    main()
