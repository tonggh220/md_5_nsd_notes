# 1 + 1 = 2
# Very Good!!!
# Continue(y/n)? y
# 97+ 65 = 100
# Wrong Answer.
# 97+ 65 = 200
# Wrong Answer.
# 97+ 65 = 300
# Wrong Answer.
# The Answer:
# 97+ 65 = 162
# Continue(y/n)? n
# Bye-bye

from random import randint, choice

def exam():
    "用于出题，让用户作答"
    # 随机选择两个数字
    nums = [randint(1, 100) for i in range(2)]
    nums.sort(reverse=True)  # 降序排列
    # nums.reverse()

    # 随机选择加减法
    op = choice('+-')

    # 计算出标准答案
    if op == '+':
        result = nums[0] + nums[1]
    else:
        result = nums[0] - nums[1]

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
