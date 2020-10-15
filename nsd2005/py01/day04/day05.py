from random import randint

nums = [randint(1, 100) for i in range(10)]
print(nums)
result1 = reversed(nums)
# print(result1)
# for i in result1:
#     print(i)
print(list(result1))
result2 = sorted(nums)
print(result2)
