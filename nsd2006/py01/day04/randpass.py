from random import choice

# 定义从哪些字符中选择
all_chs = '1234567890qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM'
# 定义用于保存结果的变量
result = ''

# 随机选出字符，并拼接到结果
for i in range(8):
    ch = choice(all_chs)
    result += ch

print(result)
