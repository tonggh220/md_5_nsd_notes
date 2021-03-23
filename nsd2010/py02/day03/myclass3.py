class Role:
    def __init__(self, name, hp, mp, weapon):
        self.name = name
        self.hp = hp
        self.mp = mp
        self.weapon = weapon

    def show_me(self):
        print(f'我是{self.name}，擅用{self.weapon}')

    def speak(self, words):
        hh = 'hehe'
        print(hh, words)

class Warrior(Role):  # 括号中的Role是该class的父类，也叫基类
    pass

class Mage(Role):
    pass

if __name__ == '__main__':
    lb = Warrior('吕布', 500, 200, '方天画戟')
    zgl = Mage('诸葛亮', 400, 300, '羽扇')
    lb.show_me()
    zgl.show_me()
