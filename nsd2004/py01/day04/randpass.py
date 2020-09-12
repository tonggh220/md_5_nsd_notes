from random import choice

# 定义在哪些字符中随机选取
all_chs = '0123456789qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM'
# 定义用于保存结果的变量
result = ''

# 随机选取8次，每次的结果拼接到result中
for i in range(8):
    ch = choice(all_chs)
    result += ch

print(result)
