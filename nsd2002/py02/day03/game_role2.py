class Role:
    def __init__(self, name, weapon):
        # 构造器方法，实例化时自动调用，注意，self不是关键字，可以是任何自定义的变量
        # 绑定在实例身上的属性，在类中任意位置可见可用
        self.name = name
        self.weapon = weapon

class Weapon:
    def __init__(self, wname, strength):
        self.wname = wname
        self.strength = strength

if __name__ == '__main__':
    ji = Weapon('方天画戟', 100)
    print(ji.wname, ji.strength)
    lb = Role('吕布', ji)
    print(lb.name, lb.weapon.wname, lb.weapon.strength)
