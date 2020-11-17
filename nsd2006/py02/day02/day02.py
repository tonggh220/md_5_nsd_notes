# def func1():
#     print('in func1')
#     func2()
#
# def func2():
#     print('in func2')
#
# func1()

from random import randint

def func1(x):
    # 整数求余，返回值只有1或0。1为真，0为假
    return x % 2

if __name__ == '__main__':
    nums = [randint(1, 100) for i in range(10)]
    print(nums)
    result1 = filter(func1, nums)
    result2 = filter(lambda x: x % 2, nums)
    print(list(result1))
    print(list(result2))
