import random

# 定义所有可用的选择
all_choice = ['石头', '剪刀', '布']
# 定义人赢的情况
win_list = [['石头', '剪刀'], ['剪刀', '布'], ['布', '石头']]
# 人机分别出拳
computer = random.choice(all_choice)
player = input('请出拳(石头/剪刀/布): ')

# 输出人机选择
print('计算机出了:%s，你出了:%s' % (computer, player))
# 判断输赢
if player == computer:
    print('\033[32;1m平局\033[0m')
elif [player, computer] in win_list:
    print('\033[31;1mYou WIN!!!\033[0m')
else:
    print('\033[31;1mYou LOSE!!!\033[0m')
