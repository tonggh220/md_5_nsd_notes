from random import choice

# 定义可用字符
all_chs = '0123456789qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM'
# 定义用于保存结果的变量
result = ''
# 从可用的字符串中选出随机字符，拼接到结果变量
for i in range(8):
    ch = choice(all_chs)
    result += ch

print(result)
