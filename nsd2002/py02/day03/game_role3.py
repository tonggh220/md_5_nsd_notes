class Role:
    def __init__(self, name, weapon):
        # 构造器方法，实例化时自动调用，注意，self不是关键字，可以是任何自定义的变量
        # 绑定在实例身上的属性，在类中任意位置可见可用
        self.name = name
        self.weapon = weapon

    def show_me(self):
        # 绑定在实例身上的属性，在类中任意位置可见可用
        print('我是%s，我擅用%s' % (self.name, self.weapon))

    def speak(self, words):
        # 没有绑定在实例身上的变量，只是局部变量，只能用在函数中
        hh = 'Hahaha'
        print(hh)
        print(words)

class Warrior(Role):  # 括号中的类是该类的父类，也叫基类
    # 子类将会直接继承父类所有的方法
    def attack(self, target):
        print('与%s近身肉搏' % target)

class Mage(Role):
    def attack(self, target):
        print('远程打击%s' % target)

if __name__ == '__main__':
    # 实例本身将会自动作为第一个参数传递，本例中是lb
    lb = Role('吕布', '方天画戟')  # 实例化，创建具体的对象
    print(lb.name, lb.weapon)
    lb.show_me()
    lb.speak('马中赤兔，人中吕布')
    zf = Warrior('张飞', '丈八蛇矛')
    zf.show_me()
    zf.speak('吾乃燕人张飞张冀德')
    zf.attack('吕布')
    zgl = Mage('诸葛亮', '羽扇')
    zgl.show_me()
    zgl.attack('曹操')
