import random
from string import ascii_letters, digits

# 定义在哪获取字符
# all_chs = '1234567890qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM'
all_chs = ascii_letters + digits

def mk_pwd(n=8):
    # 定义用于保存结果的变量
    result = ''

    # 随机获取一个字符拼接到结果变量中，取8遍
    for i in range(n):
        ch = random.choice(all_chs)
        result += ch

    return result

if __name__ == '__main__':
    p1 = mk_pwd()
    p2 = mk_pwd(4)
    print(p1)
    print(p2)
