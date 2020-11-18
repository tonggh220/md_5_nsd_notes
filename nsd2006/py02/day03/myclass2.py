class Role:
    def __init__(self, name, weapon):
        self.name = name
        self.weapon = weapon

class Weapon:
    def __init__(self, wname, strength, type):
        self.wname = wname
        self.strength = strength
        self.type = type

if __name__ == '__main__':
    ji = Weapon('方天画戟', 100, '物理伤害')
    print(ji.wname, ji.strength, ji.type)
    lb = Role('吕布', '方天画戟')
