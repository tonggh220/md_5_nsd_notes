from random import randint

# def fn(x):
#     # 对于整数n，除以2只能是1或0，1为真，0为假
#     return x % 2
#
# if __name__ == '__main__':
#     nums = [randint(1, 100) for i in range(10)]
#     print(nums)
#     result1 = filter(fn, nums)
#     print(list(result1))
#     result2 = filter(lambda x: x % 2, nums)
#     print(list(result2))

def fn(x):
    return x + 100

if __name__ == '__main__':
    nums = [randint(1, 100) for i in range(10)]
    print(nums)
    result1 = map(fn, nums)
    print(list(result1))
    result2 = map(lambda x: x + 100, nums)
    print(list(result2))
