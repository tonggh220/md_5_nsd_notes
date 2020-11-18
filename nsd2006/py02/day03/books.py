class Book:
    def __init__(self, title, author):
        # 构造器方法，实例化时自动调用
        self.title = title
        self.author = author

    def __str__(self):
        # 打印、显示实例时，返回这个方法返回的字符串
        return "《%s》" % self.title

if __name__ == '__main__':
    xyj = Book('西游记', '吴承恩')  # 调用__init__
    print(xyj)   # 调用__str__
