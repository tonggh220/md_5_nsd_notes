class Role:
    def __init__(self, name, weapon):
        "构造器方法，用于绑定数据到实例身上"
        self.name = name
        self.weapon = weapon

    def show_me(self):
        # 绑定在实例身上的属性可以在类中任何地方使用
        print('我是%s, 惯用%s' % (self.name, self.weapon))

    def speak(self, words):
        # 在方法内的变量和参数，都是局部变量
        print(words)

if __name__ == '__main__':
    # 创建实例时，自动调用__init__方法，实例本身自动作为第一个参数
    lb = Role('吕布', '方天画戟')
    print(lb.name, lb.weapon)
    lb.show_me()
    lb.speak('马中赤兔，人中吕布')
