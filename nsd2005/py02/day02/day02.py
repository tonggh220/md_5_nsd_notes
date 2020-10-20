def fn1():
    print('func 1')
    fn2()

def fn2():
    print('func 2')

if __name__ == '__main__':
    fn1()
