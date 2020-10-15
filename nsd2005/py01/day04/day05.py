# from random import randint
#
# nums = [randint(1, 100) for i in range(10)]
# print(nums)
# result1 = reversed(nums)
# print(result1)
# for i in result1:
#     print(i)
# print(list(result1))
# result2 = sorted(nums)
# print(result2)
###################################
#
# names = ['tom', 'jerry', 'jack', 'rose', 'bob']
# for i in (0, 1, 2, 3):
#     print(i, names[i])
##########
# for i in range(4):
#     print(i, names[i])
##########
# for i in range(len(names)):
#     print(i, names[i])
##########
#
names = ['tom', 'jerry', 'jack', 'rose', 'bob']
# >>> list(enumerate(names))
# [(0, 'tom'), (1, 'jerry'), (2, 'jack'), (3, 'rose'), (4, 'bob')]
# for data in enumerate(names):
#     print(data)
#############
for i, name in enumerate(names):
    print(i, name)
