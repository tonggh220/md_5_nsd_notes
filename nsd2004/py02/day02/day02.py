# def func1():
#     print('in func1')
#     func2()
#
# def func2():
#     print('in func2')
#
# if __name__ == '__main__':
#     func1()

from random import randint

def func1(x):
    return x % 2

if __name__ == '__main__':
    nums = [randint(1, 100) for i in range(10)]
    print(nums)
    result1 = filter(func1, nums)
    print(list(result1))








