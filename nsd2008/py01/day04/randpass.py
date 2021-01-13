from random import choice

# 定义可用字符集
all_chs = '1234567890qwertyuiopasdfghjkzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM'
# 创建用于保存结果的变量
result = ''
# 在可用字符集中随机选一个字符，拼接到结果变量中，共运行n次
for i in range(8):
    ch = choice(all_chs)
    result += ch

print(result)
