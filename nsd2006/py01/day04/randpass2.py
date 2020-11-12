from random import choice
from string import ascii_letters, digits

# 定义从哪些字符中选择
all_chs = ascii_letters + digits

def mk_pwd(n=8):
    # 定义用于保存结果的变量
    result = ''

    # 随机选出字符，并拼接到结果
    for i in range(n):
        ch = choice(all_chs)
        result += ch

    return result

if __name__ == '__main__':
    p1 = mk_pwd()
    p2 = mk_pwd(4)
    print(p1)
    print(p2)
