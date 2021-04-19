from random import choice
from string import ascii_letters, digits

# 定义可用字符串
ALL_CHS = ascii_letters + digits

def mk_pwd(n=8):
    # 定义用于保存结果的变量
    result = ''
    # 在可用字符串中随机选择一项，拼接到结果变量中
    for i in range(n):
        ch = choice(ALL_CHS)
        result += ch

    return result

if __name__ == '__main__':
    p1 = mk_pwd()
    n = int(input('长度: '))
    p2 = mk_pwd(n)
    print(p1)
    print(p2)
