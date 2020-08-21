class Book:
    def __init__(self, title, author):
        "构造器方法，实例化时自动调用"
        self.title = title
        self.author = author

    def __str__(self):
        "打印、显示实例时，将展示这个方法的返回值"
        return "《%s》" % self.title

    def __call__(self):
        "使实例对象可以像函数一样调用"
        print('《%s》是%s编著的' % (self.title, self.author))

if __name__ == '__main__':
    ly = Book('论语', '孔子')  # 调用__init__
    print(ly)    # 调用__str__
    ly()



