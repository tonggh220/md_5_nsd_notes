class Weapon:
    def __init__(self, wname, type, strength):
        self.wname = wname
        self.type = type
        self.strength = strength

class Role:
    def __init__(self, name, weapon):
        "构造器方法，用于绑定数据到实例身上"
        self.name = name
        self.weapon = weapon

if __name__ == '__main__':
    ji = Weapon('方天画戟', '物理', 100)
    print(ji.wname, ji.type, ji.strength)
    lb = Role('吕布', ji)
    print(lb.weapon.wname, lb.weapon.type, lb.weapon.strength)
