def func1():
    print('in func1')
    func2()

def func2():
    print('In Func2')

if __name__ == '__main__':
    func1()
