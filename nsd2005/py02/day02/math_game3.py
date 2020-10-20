from random import randint, choice

def exam():
    "出题，用户作答"
    funcs = {'+': lambda x, y: x + y, '-': lambda x, y: x - y}
    # 随机生成两个整数
    nums = [randint(1, 100) for i in range(2)]
    nums.sort(reverse=True)  # 降序排列

    # 随机选择加减法
    op = choice('+-')

    # 生成标准答案
    result = funcs[op](*nums)

    # 用户作答，判断正误
    prompt = "%s %s %s = " % (nums[0], op, nums[1])
    i = 0
    while i < 3:
        try:
            answer = int(input(prompt))
        except:  # 不填写具体的异常，可以捕获所有异常，不推荐
            print()  # 打印空行
            continue

        if answer == result:
            print('不错哟！')
            break
        print('不对哟！')
        i += 1
    else:
        print("The Answer:\n%s%s" % (prompt, result))

def main():
    "主程序代码逻辑"
    while 1:
        exam()
        try:
            yn = input("Continue(y/n)? ").strip()[0]  # 去除字符串两端空白字符后，取第一个字符
        except IndexError:
            continue
        except (KeyboardInterrupt, EOFError):
            yn = 'n'

        if yn in 'nN':
            print('\nBye-bye')
            break

if __name__ == '__main__':
    main()
