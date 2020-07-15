import random

win_list = [['石头', '剪刀'], ['剪刀', '布'], ['布', '石头']]
xuan_xiang = ['石头', '剪刀', '布']

# 为人机创建计分牌
pwin = 0
cwin = 0

while pwin < 2 and cwin < 2:
    computer = random.choice(xuan_xiang)
    player = input('请出拳(石头/剪刀/布): ')

    # 判断输赢
    print('player: %s, computer: %s' % (player, computer))
    if player == computer:
        print('\033[32;1m平局\033[0m')
    elif [player, computer] in win_list:
        print('\033[31;1mYou WIN!!!\033[0m')
        pwin += 1
    else:
        print('\033[31;1mYou LOSE!!!\033[0m')
        cwin += 1
