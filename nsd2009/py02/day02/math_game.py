from random import randint, choice

def exam():
    "用于出题，让用户作答"
    # 随机生成两个整数
    nums = [randint(1, 100) for i in range(2)]
    nums.sort(reverse=True)  # 降序
    # nums.reverse()

    # 随机选择加减法
    op = choice('+-')
    # 计算出标准答案
    if op == '+':
        result = nums[0] + nums[1]
    else:
        result = nums[0] - nums[1]

    # 用户作答，判断正误

def main():
    "主程序代码逻辑"
    while 1:
        exam()
        # 去除字符串两端空格后，取第一个字符
        choice = input("Continue(y/n)? ").strip()[0]
        if choice in 'nN':
            print('\nBye-bye')
            break

if __name__ == '__main__':
    main()
