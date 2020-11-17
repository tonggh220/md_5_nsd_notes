from random import randint, choice

def add(x, y):
    return x + y

def sub(x, y):
    return x - y

def exam():
    "出题，用户作答"
    funcs = {'+': add, '-': sub}
    # 随机取出2个数字
    nums = [randint(1, 100) for i in range(2)]
    nums.sort(reverse=True)  # 降序排列

    # 随机选出加减法
    op = choice('+-')
    # 计算出标准答案
    result = funcs[op](*nums)

    # 用户作答，判断对错
    i = 0
    prompt = '%s %s %s = ' % (nums[0], op, nums[1])
    while i < 3:
        try:
            answer = int(input(prompt))
        except:  # 不指定异常，可以捕获所有异常，不推荐
            print()
            continue

        if answer == result:
            print("不错哟～")
            break
        print("不对哟～")
        i += 1
    else:
        print("正确答案是：\n%s%s" % (prompt, result))

def main():
    "主程序代码逻辑"
    while 1:
        exam()
        try:
            yn = input("Continue(Y/n)? ").strip()[0]  # 去除两端空格后，取第一个字符
        except (KeyboardInterrupt, EOFError):
            yn = 'n'
        except IndexError:
            continue

        if yn in 'nN':
            print('\nBye-bye')
            break

if __name__ == '__main__':
    main()
