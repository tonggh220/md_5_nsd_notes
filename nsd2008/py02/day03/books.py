class Book:
    def __init__(self, title, author):
        "构造器方法，实例化时自动调用"
        self.title = title
        self.author = author

    def __str__(self):
        "打印、显示实例时，将展示这个方法返回的字符串"
        return '《%s》' % self.title

if __name__ == '__main__':
    linux = Book('Linux运维之道', '丁明一')  # 调用__init__
    print(linux)  # 调用__str__


