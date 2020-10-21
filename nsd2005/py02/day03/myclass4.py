class Role:
    def __init__(self, name, weapon):
        # 构造器方法，实例化自动调用时，注意，self不是关键字，可以是任何自定义的变量
        # 绑定在实例身上的属性，在类中任意位置可见可用
        self.name = name
        self.weapon = weapon

    def show_me(self):
        # 绑定在实例身上的属性，在类中任意位置可见可用
        print('我是%s，擅用%s' % (self.name, self.weapon))

    def speak(self, words):
        # 没有绑定在实例身上的变量，只是局部变量，只能用在函数中
        hh = 'Hahaha'
        print(hh)
        print(words)

class Warrior(Role):
    def attack(self, target):
        print('与%s近身肉搏' % target)

class Mage(Role):
    def attack(self, target):
        print('远程打击%s' % target)

if __name__ == '__main__':
    lb = Warrior('吕布', '方天画戟')  # 实例化，创建具体的实例对象
    lb.speak('马中赤兔，人中吕布')
    zgl = Mage('诸葛亮', '羽扇')
    zgl.show_me()
    lb.attack('关羽')
    zgl.attack('曹操')
