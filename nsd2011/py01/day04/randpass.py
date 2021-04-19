from random import choice

# 定义可用字符串
all_chs = '01234567890qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM'
# 定义用于保存结果的变量
result = ''
# 在可用字符串中随机选择一项，拼接到结果变量中
for i in range(8):
    ch = choice(all_chs)
    result += ch
# 输出结果
print(result)
