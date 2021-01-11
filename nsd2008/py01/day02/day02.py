# if 3 > 0:
#     print('yes')
#     print('ok')
#
# s1 = 'python'
# if 'th' in s1:
#     print('yeah')

# if 0.0:
#     print('任何值为0的数字都是假')
#
# if ' ':
#     print('空格字符也是一个字符，为真')
#
# if []:
#     print('空列表，为假')
#
# if (10, 20):
#     print('非空元组，为真')
#
# if {'name': 'nb'}:
#     print('非空字典，为真')

# if ['']:
#     print('列表中有一个字符串，所以是非空列表，为真')
##################################

# a = 10
# b = 20
#
# if a < b:
#     s1 = a
# else:
#     s1 = b
# print(s1)
#
# 上面的写法，可简化为
a = 10
b = 20
s2 = a if a < b else b
##################################
print(s2)

