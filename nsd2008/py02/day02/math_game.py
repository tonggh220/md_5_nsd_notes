# 1 + 1 = 2
# Very Good!!!
# Continue(y/n)? y
# 28 + 36 = 40
# Wrong Answer!!!
# 28 + 36 = 100
# Wrong Answer!!!
# 28 + 36 = 50
# Wrong Answer!!!
# The Answer: 28 + 36 = 64
# Continue(y/n)? n
# Bye-bye

from random import randint, choice

def exam():
    "用于出题，用户作答"
    # 随机生成两个数字，并降序排列
    nums = [randint(1, 100) for i in range(2)]
    nums.sort(reverse=True)
    # nums.reverse()
    # 随机选择加减法
    op = choice('+-')
    # 计算出标准答案
    if op == '+':
        result = nums[0] + nums[1]
    else:
        result = nums[0] - nums[1]
    # 用户作答，判断对错
    prompt = '%s %s %s = ' % (nums[0], op, nums[1])
    answer = int(input(prompt))
    if answer == result:
        print('Very Good!!!')
    else:
        print('Wrong Answer!!!')

def main():
    "用于主程序代码逻辑"
    while 1:
        exam()
        # 去除字符串两端空格后，取出第一个字符
        yn = input("Continue(y/n)? ").strip()[0]
        if yn in 'nN':
            print('\nBye-bye')
            break

if __name__ == '__main__':
    main()






