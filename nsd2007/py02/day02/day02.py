# def func1():
#     print('in func1')
#     func2()
#
# def func2():
#     print('In Func2')
#
# if __name__ == '__main__':
#     func1()

from random import randint

def func1(x):
    return x % 2  # x%2的结果只有1和0两种情况，0为假，非0为真

if __name__ == '__main__':
    nums = [randint(1, 100) for i in range(10)]
    print(nums)
    # 把nums中的偶数过虑掉
    result1 = filter(func1, nums)
    print(list(result1))











