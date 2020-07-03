def func1():
    print('Hello func1')

def func2():
    print('Welcome func2')

if __name__ == '__main__':
    funcs1 = {'0': func1, '1': func2}
    funcs2 = {'0': func1(), '1': func2()}
    print(funcs1)
    print(funcs2)
