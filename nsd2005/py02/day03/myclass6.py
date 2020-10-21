class A:
    def func1(self):
        print('A func1')

class B:
    def func2(self):
        print('B func2')

class C(A, B):
    pass

if __name__ == '__main__':
    c1 = C()
    c1.func1()
    c1.func2()
