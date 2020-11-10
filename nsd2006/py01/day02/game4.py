import random

# 人机进行选择
all_choices = ['石头', '剪刀', '布']
win_list = [['石头', '剪刀'], ['剪刀', '布'], ['布', '石头']]  # 定义人赢的情况
prompt = """(0) 石头
(1) 剪刀
(2) 布
请选择(0/1/2): """
pwin = 0  # 定义人机胜利计数器
cwin = 0

while pwin < 2 and cwin < 2:
    computer = random.choice(all_choices)
    ind = int(input(prompt))   # 获取用户输入的数字并转成整数
    player = all_choices[ind]  # 在列表中通过下标取出对应的字符串

    # 输出人机选择
    print('你出了:%s, 计算机出:%s' % (player, computer))

    # 判断胜负
    if player == computer:
        print('\033[32;1m平局\033[0m')
    elif [player, computer] in win_list:  # 人机选择组成的小列表是大列表中的一项
        pwin += 1
        print('\033[31;1mYou WIN!!!\033[0m')
    else:
        cwin += 1
        print('\033[31;1mYou LOSE!!!\033[0m')
