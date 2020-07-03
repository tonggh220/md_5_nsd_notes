from random import choice

# 定义可用的字符
all_chs = '1234567890qwertyuiopasdfghjklxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM'
# 定义用于保存结果的变量
result = ''

# 取出一个随机字符拼接到result，取８次
for i in range(8):
    ch = choice(all_chs)
    result += ch

print(result)
