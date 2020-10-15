import random

# 定义在哪获取字符
all_chs = '1234567890qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM'

# 定义用于保存结果的变量
result = ''

# 随机获取一个字符拼接到结果变量中，取8遍
for i in range(8):
    ch = random.choice(all_chs)
    result += ch

print(result)
