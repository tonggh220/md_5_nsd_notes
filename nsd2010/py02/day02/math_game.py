# 1 + 1 = 2
# Very Good!
# Continue(Y/n): yes
# 87 - 65 = 10
# Wrong Answer
# 87 - 65 = 20
# Wrong Answer
# 87 - 65 = 1
# Wrong Answer
# The Answer:
# 87 - 65 = 22
# Continue(Y/n): n
# Bye-bye

from random import randint, choice

def exam():
    '用于出题，用户作答'
    # 随机生成两个整数
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

    # 用户作答，判断正误
    prompt = f'{nums[0]} {op} {nums[1]} = '
    n = 0

    while n < 3:
        answer = int(input(prompt))
        if answer == result:
            print('你真棒!!!')
            break
        print('不对哟!!!')
        n += 1
    else:
        print(f'正确答案是:\n{prompt}{result}')

def main():
    '主程序代码逻辑'
    while 1:
        exam()
        yn = input('Continue(Y/n)? ').strip()[0]  # 取出用户输入的第一个非空字符
        if yn in 'nN':
            print('\nBye-bye')
            break

if __name__ == '__main__':
    main()
