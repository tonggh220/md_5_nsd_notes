# 1 + 1 = 2
# Very Good!
# Continue(y/n)? yes
# 18 + 25 = 30
# Wrong Answer
# 18 + 25 = 40
# Wrong Answer
# 18 + 25 = 50
# Wrong Answer
# The Answer:
# 18 + 25 = 43
# Continue(y/n)? n
# Bye-bye

from random import randint, choice

def exam():
    "出题，用户作答"
    # 随机选择2个整数并降序排列
    nums = [randint(1, 100) for i in range(2)]
    nums.sort(reverse=True)  # 降序排列
    # nums.sort()
    # nums.reverse()
    # 随机选择加减法
    op = choice('+-')
    # 计算出标准答案
    if op == '+':
        result = nums[0] + nums[1]
    else:
        result = nums[0] - nums[1]

    # 用户作答，判断正误
    prompt = '%s %s %s = ' % (nums[0], op, nums[1])  # 拼接出算式
    n = 0
    while n < 3:
        answer = int(input(prompt))
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
        yn = input("Continue(y/n)? ").strip()[0]  # 取用户输入的第一个非空格字符
        if yn in 'nN':
            print('\nBye-bye')
            break

if __name__ == '__main__':
    main()
