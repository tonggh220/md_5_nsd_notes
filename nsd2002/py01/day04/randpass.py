from random import choice

# 定义从哪取随机字符
chs = '1234567890qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM'

# 定义用于保存结果的变量
result = ''

# 在可用的字符串中随机取一个字符，拼接到结果变量中
for i in range(8):
    ch = choice(chs)
    result += ch

# 打印结果，查看是否满足要求
print(result)
