'''
1 + 1 = 2
Very Good!!!
Continue(Y/n)? y
34 + 52 = 100
Wrong Answer!!!
34 + 52 = 10
Wrong Answer!!!
34 + 52 = 200
Wrong Answer!!!
The Answer:
34 + 52 = 86
Continue(Y/n)? no
Bye-bye
'''
from random import randint, choice

def exam():
    '用于出题，用户作答'
    # 随机生成两个数字
    nums = [randint(1, 100) for i in range(2)]
    nums.sort(reverse=True)  # 降序排列
    # nums.reverse()
    # 随机取出加减号
    op = choice('+-')
    # 计算出标准答案
    if op == '+':
        result = nums[0] + nums[1]
    else:
        result = nums[0] - nums[1]

    i = 0
    # 用户作答
    prompt = f'{nums[0]} {op} {nums[1]} = '
    while i < 3:
        answer = int(input(prompt))
        if answer == result:
            print('Very Good!!!')
            break
        print('Wrong Answer!!!')
        i += 1
    else:
        print('The Answer:\n', f'{prompt}{result}')

def main():
    '主程序代码逻辑'
    while 1:
        exam()
        yn = input('Continue(Y/n)? ').strip()[0]  # 取出第一个字符
        if yn in 'nN':
            print('\nBye-bye')
            break

if __name__ == '__main__':
    main()
