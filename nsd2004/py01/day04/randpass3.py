from random import choice
from string import ascii_letters, digits

# 定义在哪些字符中随机选取
all_chs = ascii_letters + digits

def mk_pwd(n=8):
    # 定义用于保存结果的变量
    result = ''

    # 随机选取n次，每次的结果拼接到result中
    for i in range(n):
        ch = choice(all_chs)
        result += ch

    return result

if __name__ == '__main__':
    a1 = mk_pwd()
    a2 = mk_pwd(4)
    print(a1)
    print(a2)
