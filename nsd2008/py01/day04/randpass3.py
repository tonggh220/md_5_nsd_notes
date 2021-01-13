from random import choice
from string import ascii_letters, digits

# 定义可用字符集
all_chs = ascii_letters + digits

def mk_pwd(n=8):
    # 创建用于保存结果的变量
    result = ''
    # 在可用字符集中随机选一个字符，拼接到结果变量中，共运行n次
    for i in range(n):
        ch = choice(all_chs)
        result += ch

    return result

if __name__ == '__main__':
    l = int(input("密码位数: "))
    p1 = mk_pwd(l)
    print(p1)
