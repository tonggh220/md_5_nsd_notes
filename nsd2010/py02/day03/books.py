class Book:
    def __init__(self, title, author):
        # 构造器方法，实例化时自动调用，用于绑定属性
        self.title = title
        self.author = author

    def __str__(self):
        '打印、显示实例时，展示该方法返回的字符串'
        return f'《{self.title}》'

    def __call__(self):
        '当实例像函数一样调用时，执行此方法中的代码'
        print(f'《{self.title}》是{self.author}编写的')

if __name__ == '__main__':
    pybook = Book('例解Python', '张志刚')  # 自动调用__init__
    print(pybook)                         # 自动调用__str__
    pybook()                              # 自动调用__call__
