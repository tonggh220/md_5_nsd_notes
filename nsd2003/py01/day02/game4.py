import random

# 定义所有可用的选择
all_choice = ['石头', '剪刀', '布']
# 定义人赢的情况
win_list = [['石头', '剪刀'], ['剪刀', '布'], ['布', '石头']]
prompt = """(0) 石头
(1) 剪刀
(2) 布
请选择(0/1/2): """
pwin = 0  # 用于记录人赢的次数
cwin = 0  # 用于记录计算机赢的次数

while pwin < 2 and cwin < 2:  # 人机都没有赢够两次则继续
    # 人机分别出拳
    computer = random.choice(all_choice)
    ind = int(input(prompt))  # 用户输入的数字正好是all_choice的下标
    player = all_choice[ind]

    # 输出人机选择
    print('计算机出了:%s，你出了:%s' % (computer, player))
    # 判断输赢
    if player == computer:
        print('\033[32;1m平局\033[0m')
    elif [player, computer] in win_list:
        pwin += 1
        print('\033[31;1mYou WIN!!!\033[0m')
    else:
        cwin += 1
        print('\033[31;1mYou LOSE!!!\033[0m')
