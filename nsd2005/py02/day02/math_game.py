# 10 + 8 = 18
# Very Good!
# Continue(y/n)? y
# 23 + 12 = 30
# Wrong Answer!
# 23 + 12 = 40
# Wrong Answer!
# 23 + 12 = 50
# Wrong Answer!
# The Answer:
# 23 + 12 = 35
# Continue(y/n)? n
# Bye-bye

from random import randint, choice

def exam():
    "出题，用户作答"
    # 随机生成两个整数
    nums = [randint(1, 100) for i in range(2)]
    nums.sort(reverse=True)  # 降序排列
    # nums.reverse()

    # 随机选择加减法
    op = choice('+-')

    # 生成标准答案
    if op == '+':
        result = nums[0] + nums[1]
    else:
        result = nums[0] - nums[1]

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






