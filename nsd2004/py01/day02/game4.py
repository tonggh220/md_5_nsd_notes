import random

all_choices = ['石头', '剪刀', '布']  # 定义所有可用选项
# 定义人可以取胜的列表
win_list = [['石头', '剪刀'], ['剪刀', '布'], ['布', '石头']]
prompt = """(0) 石头
(1) 剪刀
(2) 布
请选择(0/1/2): """
pwin = 0  # 玩家的计分牌
cwin = 0  # 计算机的计分牌

while pwin < 2 and cwin < 2:
    # 人机分别进行选择
    computer = random.choice(all_choices)
    ind = int(input(prompt))  # 用户的选择，实际上是all_choice的下标
    player = all_choices[ind]
    # 打印人机选择
    print('你出了: %s, 计算机出了:%s' % (player, computer))

    # 判断胜负
    if player == computer:
        print('\033[32;1m平局\033[0m')
    elif [player, computer] in win_list:
        print('\033[31;1mYou WIN!!!\033[0m')
        pwin += 1
    else:
        print('\033[31;1mYou LOSE!!!\033[0m')
        cwin += 1
