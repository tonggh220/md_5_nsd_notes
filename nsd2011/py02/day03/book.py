class Book:
    def __init__(self, title, author):
        '构造器方法，实例化时自动调用'
        self.title = title
        self.author = author

    def __str__(self):
        '打印、显示实例时，展示这个方法返回的字符串'
        return f'《{self.title}》'

    def __call__(self):
        '将实例作为函数调用时，执行此方法'
        print(f'《{self.title}》是{self.author}编写的')

if __name__ == '__main__':
    linux = Book('运维之道', '丁明一')  # 调用__init__
    print(linux)      # 调用__str__
    linux()           # 调用__call__
