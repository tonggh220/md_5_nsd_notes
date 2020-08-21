class Role:
    def __init__(self, name, weapon):
        # 构造器方法，实例化时自动调用，注意，self不是关键字，可以是任何自定义的变量
        # 绑定在实例身上的属性，在类中任意位置可见可用
        self.name = name
        self.weapon = weapon

    def show_me(self):
        print('我是%s，我擅用%s' % (self.name, self.weapon))

if __name__ == '__main__':
    lb = Role('吕布', '方天画戟')
    print(lb.name, lb.weapon)
    lb.show_me()


