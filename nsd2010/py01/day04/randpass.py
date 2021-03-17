from random import choice

# 定义用于保存结果的变量
result = ''
# 定义所有可用的字符
all_chs = '0123456789qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM'
# 从可用字符中随机选取一个字符，选8次，拼接到一起
for i in range(8):
    ch = choice(all_chs)
    result += ch
# 输出结果
print(result)
