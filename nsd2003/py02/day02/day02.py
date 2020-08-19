# def func1():
#     print('fn 1')
#     func2()
#
# def func2():
#     print('fn 2')
#
# if __name__ == '__main__':
#     func1()

from random import randint

def func1(x):
    return x % 2  # 整数求余，只有0或1两种情况，0为假，1为真

if __name__ == '__main__':
    nums = [randint(1, 100) for i in range(10)]
    result1 = filter(func1, nums)
    result2 = filter(lambda x: x % 2, nums)
    print(nums)
    print(list(result1))
    print(list(result2))









