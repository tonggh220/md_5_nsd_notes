# s1 = 'Python'

# for i in range(len(s1)):  # [0, 1, 2, 3, 4, 5]
#     print(i, s1[i])

# for data in enumerate(s1):
#     print(data)  # data是由下标和下标对应字符构成的元组
#
# for i, ch in enumerate(s1):
#     print(i, ch)  # 可以将元组中的两项内容分别赋值给两个变量

s1 = '123a45'
for ch in s1:
    if ch not in '1234567890':
        print('no')
        break
else:
    print('yes')
