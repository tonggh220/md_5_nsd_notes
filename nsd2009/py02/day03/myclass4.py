class Role:
    def __init__(self, name, weapon, hp=500, mp=300):
        """被称作构造器方法，实例化时自动调用。
        self不是关键字，用任意名称都可以
        当创建时例时，用于将属性绑定到实例身上
        """
        self.name = name
        self.weapon = weapon
        self.hp = hp
        self.mp = mp

class Warrior(Role):
    def __init__(self, name, weapon, qq, hp=500, mp=300):
        # self.name = name
        # self.weapon = weapon
        # self.hp = hp
        # self.mp = mp
        # ------------------------------
        # 以上赋值已经在父类中实现过，可以用以下方法进行简化
        # Role.__init__(self, name, weapon, hp=500, mp=300)
        # ------------------------------
        # 上面明确调用父类方法的作法，也可以用super来实现
        super(Warrior, self).__init__(name, weapon, hp=500, mp=300)
        self.qq = qq

if __name__ == '__main__':
    lb = Warrior('吕布', '方天画戟', '2354436')
    print(lb.name, lb.qq)
