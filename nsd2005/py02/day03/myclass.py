class Role:
    pass

if __name__ == '__main__':
    lb = Role()  # 实例化，创建具体的实例对象
    lb.name = '吕布'
    lb.weapon = '方天画戟'
    print(lb.name, lb.weapon)
