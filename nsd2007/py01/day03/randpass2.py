from random import choice

all_chs = '1234567890qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM'

def mk_pwd(n=8):
    result = ''

    for i in range(n):
        ch = choice(all_chs)
        result += ch

    return result

if __name__ == '__main__':
    p1 = mk_pwd()
    p2 = mk_pwd(4)
    print(p1)
    print(p2)
