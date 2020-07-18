from random import choice
from string import ascii_letters, digits

# 定义从哪取随机字符
chs = ascii_letters + digits

def mk_pwd(n=8):
    # 定义用于保存结果的变量
    result = ''
    # 在可用的字符串中随机取一个字符，拼接到结果变量中
    for i in range(n):
        ch = choice(chs)
        result += ch

    return result

if __name__ == '__main__':
    # 打印结果，查看是否满足要求
    s1 = mk_pwd()
    s2 = mk_pwd(4)
    print(s1)
    print(s2)
