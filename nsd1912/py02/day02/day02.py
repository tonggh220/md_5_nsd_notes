# def func1():
#     print('Hello func1')
#     func2()
#
# def func2():
#     print('hello func2')
#
# if __name__ == '__main__':
#     func1()

# from random import randint
#
# def func1(x):
#     # 结果要不是1，要么是0。1为真，0为假
#     return x % 2
#
# if __name__ == '__main__':
#     nums = [randint(1, 100) for i in range(10)]
#     print(nums)
#     result1 = filter(func1, nums)
#     print(list(result1))
#     result2 = filter(lambda x: x % 2, nums)
#     print(list(result2))

from random import randint

def func1(x):
    return x + 1

if __name__ == '__main__':
    nums = [randint(1, 100) for i in range(10)]
    print(nums)
    result1 = map(func1, nums)
    print(list(result1))
    result2 = map(lambda x: x + 1, nums)
    print(list(result2))
