from random import choice
from string import ascii_letters, digits

all_chs = ascii_letters + digits

def mk_pwd(n=8):
    result = ''

    for i in range(n):
        ch = choice(all_chs)
        result += ch

    return result

if __name__ == '__main__':
    a = mk_pwd()
    print(a)
    b = mk_pwd(4)
    print(b)
