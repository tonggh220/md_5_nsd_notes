from random import randint

def fn(x):
    # 对于整数n，除以2只能是1或0，1为真，0为假
    return x % 2

if __name__ == '__main__':
    nums = [randint(1, 100) for i in range(10)]
    print(nums)
    result1 = filter(fn, nums)
    print(list(result1))
