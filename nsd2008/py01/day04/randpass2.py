from random import choice

def mk_pwd(n=8):
    # 定义可用字符集
    all_chs = '1234567890qwertyuiopasdfghjkzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM'
    # 创建用于保存结果的变量
    result = ''
    # 在可用字符集中随机选一个字符，拼接到结果变量中，共运行n次
    for i in range(n):
        ch = choice(all_chs)
        result += ch

    return result

if __name__ == '__main__':
    p1 = mk_pwd()
    p2 = mk_pwd(4)
    print(p1)
    print(p2)
