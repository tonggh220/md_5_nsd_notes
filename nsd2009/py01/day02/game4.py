import random

# 定义计算机可用的选择
all_choice = ['石头', '剪刀', '布']
# 定义人的胜利列表
win_list = [['石头', '剪刀'], ['剪刀', '布'], ['布', '石头']]
# 定义屏幕菜单
prompt = """(0) 石头
(1) 剪刀
(2) 布
请选择(0/1/2): """

cwin = 0  # 计算机的计分牌
pwin = 0  # 人的计分牌

while cwin < 2 and pwin < 2:  # 当人和计算机都没赢够2次，则继续
    # 计算机随机出拳
    computer = random.choice(all_choice)
    # 人出拳
    i = int(input(prompt))  # 将用户输入的字符转成数字
    player = all_choice[i]
    # 输出人机选择
    print("Your choice: %s, Computer's choice: %s" % (player, computer))

    # 判断胜负
    if player == computer:
        print('\033[32;1m平局\033[0m')
    elif [player, computer] in win_list:  # 人机选择组成的列表，正好是胜利列表的一项
        pwin += 1
        print('\033[31;1mYou WIN!!!\033[0m')
    else:
        cwin += 1
        print('\033[31;1mYou LOSE!!!\033[0m')
