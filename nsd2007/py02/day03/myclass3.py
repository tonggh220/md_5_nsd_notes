class Role:
    def __init__(self, name, weapon, hp=500, mp=300):
        # 被称作构造器方法，实例化时自动调用。self不是关键字，用任意名称都可以
        # 当创建时例时，用于将属性绑定到实例身上
        self.name = name
        self.weapon = weapon
        self.hp = hp
        self.mp = mp

    def show_me(self):
        # 绑定在实例身上的方法，在类中任意位置可见可用
        print('我是%s，擅用%s' % (self.name, self.weapon))

    def speak(self, words):
        # 没有绑在实例身上的变量，只是函数的局部变量，只能用在当前函数中
        hh = '呵呵'
        print(hh)
        print(words)

class Warrior(Role):  # Warrior是Role的子类。Role叫父类或基类
    # 子类直接拥有父类的属性和方法
    def attack(self, target):
        print('与%s近身肉搏' % target)

class Mage(Role):
    def attack(self, target):
        print('远程打击%s' % target)

if __name__ == '__main__':
    lb = Warrior('吕布', '方天画戟')
    zgl = Mage('诸葛亮', '羽扇', 300, 500)
    lb.show_me()
    lb.attack('刘备')
    zgl.attack('曹操')
