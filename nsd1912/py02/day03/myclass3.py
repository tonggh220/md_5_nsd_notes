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

class Warrior(Role):
    def attack(self, target):
        print('与%s近身肉搏' % target)

class Mage(Role):
    def attack(self, target):
        print('远程打击%s' % target)

if __name__ == '__main__':
    lb = Warrior('吕布', '方天画戟')
    zgl = Mage('诸葛亮', '羽扇')
    lb.show_me()
    zgl.show_me()
    lb.attack('张飞')
    zgl.attack('曹操')
