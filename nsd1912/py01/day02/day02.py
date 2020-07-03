# if 10 > 3:
#     print('Yes')
#     print('OK')
#
# if -0.0:
#     print('值为0，假')
#
# if 100:
#     print('非0值为真')
#
# if ' ':
#     print('空格也是一个字符，为真')
#
# if '':
#     print('长度为0的字符串才是空串，为假')
#
# if None:
#     print('None表示空，为假')
#
# if not []:
#     print('空列表为假，取反为真')

a = 10
b = 20
if a < b:
    s1 = a
else:
    s1 = b
# 以上代码可以简写为
s2 = a if a < b else b
print(s1)
print(s2)













