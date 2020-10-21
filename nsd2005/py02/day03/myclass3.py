class Weapon:
    def __init__(self, wname, type, strength):
        self.wname = wname
        self.type = type
        self.strength = strength

if __name__ == '__main__':
    ji = Weapon('方天画戟', '物理攻击', 100)
    print(ji.wname, ji.type, ji.strength)
