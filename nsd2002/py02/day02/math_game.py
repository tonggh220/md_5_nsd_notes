# 1 + 1 = 2
# Very Good!
# Continue(y/n)? y
# 83 + 65 = 100
# Wrong Answer.
# 83 + 65 = 200
# Wrong Answer.
# 83 + 65 = 150
# Wrong Answer.
# Answer: 83 + 65 = 148
# Continue(y/n)? No
# Bye-bye

from random import randint, choice

def exam():
    "出题，用户作答"
    # 随机生成2个数字
    nums = [randint(1, 100) for i in range(2)]
    nums.sort(reverse=True)  # 降序排列

    # 随机选择加减法
    op = choice('+-')

    # 计算出标准答案
    if op == '+':
        result = nums[0] + nums[1]
    else:
        result = nums[0] - nums[1]

    # 用户作答
    prompt = '%s %s %s = ' % (nums[0], op, nums[1])
    answer = int(input(prompt))
    if answer == result:
        print('不错哟!!!')
    else:
        print('不对哟!!!')

    print('Answer: %s%s' % (prompt, result))

def main():
    "程序的代码逻辑"
    while 1:
        exam()
        # 获取用户输入，去除两端空格再取出第一个字符
        yn = input('Continue(y/n)? ').strip()[0]
        if yn in 'Nn':
            print('\nBye-bye')
            break

if __name__ == '__main__':
    main()







