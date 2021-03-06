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

if __name__ == '__main__':
    lb = Role('吕布', '方天画戟')  # 自动调用__init__，创建具体的实例对象
    print(lb.name, lb.weapon, lb.hp, lb.mp)
    lb.show_me()
    lb.speak('马中赤兔，人中吕布')
    zf = Role('张飞', '丈八蛇矛')
    zf.show_me()
    zf.speak('吾乃燕人张飞张翼德')
