# def func1():
#     print('in func1')
#     func2()
#
# def func2():
#     print('in func2')
#
# if __name__ == '__main__':
#     func1()

# from random import randint
#
# def func1(x):
#     return x % 2   # x%2的结果只有1和0两种情况，1为真0为假
#
# if __name__ == '__main__':
#     nums = [randint(1, 100) for i in range(10)]
#     print(nums)
#     result = filter(func1, nums)
#     result2 = filter(lambda x: x % 2, nums)
#     print(list(result))
#     print(list(result2))

from random import randint

def func1(x):
    return x + 100

if __name__ == '__main__':
    nums = [randint(1, 100) for i in range(10)]
    print(nums)
    result = map(func1, nums)
    result2 = map(lambda x: x + 100, nums)
    print(list(result))
    print(list(result2))

