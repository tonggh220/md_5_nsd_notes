# s1 = 'Python'

# for i in [0, 1, 2, 3, 4, 5]:
#     print(i, s1[i])

# for i in range(6):
#     print(i, s1[i])

# for i in range(len(s1)):
#     print(i, s1[i])

# l1 = [10, 15, 20, 10, 30, 10, 4, 10]
# for i in range(len(l1)):
#     if 10 in l1:
#         l1.remove(10)
#     else:
#         break
# print(l1)

# l1 = [10, 15, 20, 10, 30, 10, 4, 10]
# for i in range(len(l1)):
#     if 10 not in l1:
#         break
#     l1.remove(10)
# print(l1)

l1 = [10, 15, 20, 10, 30, 10, 4, 10]
while 1:
    if 10 not in l1:
        break
    l1.remove(10)
print(l1)

