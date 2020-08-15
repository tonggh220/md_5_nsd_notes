from random import choice

# 定义用于选择字符的字符串
all_chs = '1234567890qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM'
# 声明用于保存结果的变量
result = ''
# 循环，每次取出的字符拼接到结果变量
for i in range(8):
    ch = choice(all_chs)
    result += ch

print(result)
