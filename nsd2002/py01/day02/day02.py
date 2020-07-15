# if 3 > 0:
#     print('yes')
#
# print('*' * 30)
#
# a = 10
# if a > 100:
#     print('yes')
# else:
#     print('no')

# if -0.0:
#     print('值为0，假')
#
# if ' ':
#     print('空格也是一个字符，为真')
#
# if '':
#     print('空字符串，假')
#
# if [10, 20]:
#     print('非空列表，为真')
#
# if (10, 20):
#     print('非空元组，为真')

a = 10
b = 20
if a < b:
    s = a
else:
    s = b
print(s)

s1 = a if a < b else b
print(s1)
