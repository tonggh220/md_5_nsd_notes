class Role:
    def __init__(self, name, weapon, hp=500, mp=300):
        # 被称作构造器方法，实例化时自动调用
        # self不是关键字，可以是自定义的任何名字，表示实例本身
        # 当创建实例时，用于将属性绑定到实例身上
        self.name = name
        self.weapon = weapon
        self.hp = hp
        self.mp = mp

    def show_me(self):
        # 绑定在实例身上的属性，在类中任意位置可见可用
        print(f'我是{self.name}，擅用{self.weapon}')

    def speak(self, words):
        # 没有绑在实例身上的属性，就是局部变量，只能在当前函数中使用
        hh = '呵呵'
        print(hh, words)

class Warrior(Role):  # 括号中的Role是父类或基类
    'Role的子类'
    def attack(self, target):
        print(f'与{target}近身肉搏')

class Mage(Role):
    'Role的子类'
    def attack(self, target):
        print(f'远程打击{target}')

if __name__ == '__main__':
    lb = Warrior('吕布', '方天画戟')
    zgl = Mage('诸葛亮', '羽扇')
    lb.show_me()
    lb.speak('马中赤兔，人中吕布')
    zgl.show_me()
    zgl.speak('大梦谁先觉，平生我自知。')
    lb.attack('董卓')
    zgl.attack('曹操')
