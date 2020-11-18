class Role:
    def __init__(self, name, weapon):
        self.name = name
        self.weapon = weapon

    def show_me(self):
        print('我是%s，擅用%s' % (self.name, self.weapon))

    def speak(self, words):
        hh = 'Hahahahahaha'
        print(hh)
        print(words)

class Warrior(Role):  # 括号中的类是该类的父类，也称作基类
    pass

if __name__ == '__main__':
    lb = Warrior('吕布', '方天画戟')  # 实例化，通过类创建具体的实例对象
    lb.show_me()
    lb.speak('马中赤兔，人中吕布')
    zf = Warrior('张飞', '丈八蛇矛')
    zf.show_me()
    zf.speak('我是燕人张飞张冀德')
