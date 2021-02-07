from random import choice
from string import ascii_letters, digits

# 定义可用字符
all_chs = ascii_letters + digits

def mk_pwd(n=8):
    # 定义用于保存结果的变量
    result = ''
    # 从可用的字符串中选出随机字符，拼接到结果变量
    for i in range(n):
        ch = choice(all_chs)
        result += ch

    return result

if __name__ == '__main__':
    p1 = mk_pwd()
    p2 = mk_pwd(4)
    print(p1)
    print(p2)
