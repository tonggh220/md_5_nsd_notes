# def func1():
#     print('fn 1')
#     func2()
#
# def func2():
#     print('fn 2')
#
# if __name__ == '__main__':
#     func1()

# from random import randint
#
# def func1(x):
#     return x % 2  # 整数求余，只有0或1两种情况，0为假，1为真
#
# if __name__ == '__main__':
#     nums = [randint(1, 100) for i in range(10)]
#     result1 = filter(func1, nums)
#     result2 = filter(lambda x: x % 2, nums)
#     print(nums)
#     print(list(result1))
#     print(list(result2))

# from random import randint

# def func1(x):
#     return x + 100
#
# if __name__ == '__main__':
#     nums = [randint(1, 100) for i in range(10)]
#     print(nums)
#     result1 = map(func1, nums)
#     result2 = map(lambda x: x + 100, nums)
#     print(list(result1))
#     print(list(result2))


# 创建一个取之不尽的数字生成器
def gen_num():
  n = 0
  while 1:
    yield n
    n += 1

nums = gen_num()

i = 0
while i < 10:
  data = nums.__next__()  # 生成器生成数字时，内部采用的方法
  print(data)
  i += 1





