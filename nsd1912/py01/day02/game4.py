import random

all_choices = ['石头', '剪刀', '布']
win_list = [['石头', '剪刀'], ['剪刀', '布'], ['布', '石头']]
prompt = '''(0) 石头
(1) 剪刀
(2) 布
请选择(0/1/2): '''
# 创建人机的计分牌
pwin = 0
cwin = 0

while pwin < 2 and cwin < 2:  # 人机都没赢够两次则继续
    computer = random.choice(all_choices)
    i = int(input(prompt))    # 将用户输入的012转成数字
    player = all_choices[i]   # 在列表中通过下标取出石头、剪刀、布

    # 输出人机选择
    print('你出拳: %s, 计算机出拳: %s' % (player, computer))

    # 判断胜负
    if player == computer:
        print('\033[32;1m平局\033[0m')
    elif [player, computer] in win_list:
        pwin += 1
        print('\033[31;1mYou WIN!!!\033[0m')
    else:
        cwin += 1
        print('\033[31;1mYou LOSE!!!\033[0m')
