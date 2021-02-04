import random

# 定义计算机可用的选择
all_choice = ['石头', '剪刀', '布']
# 定义人的胜利列表
win_list = [['石头', '剪刀'], ['剪刀', '布'], ['布', '石头']]
# 计算机随机出拳
computer = random.choice(all_choice)
# 人出拳
player = input("请出拳(石头/剪刀/布): ")
# 输出人机选择
print("Your choice: %s, Computer's choice: %s" % (player, computer))

# 判断胜负
if player == computer:
    print('\033[32;1m平局\033[0m')
elif [player, computer] in win_list:  # 人机选择组成的列表，正好是胜利列表的一项
    print('\033[31;1mYou WIN!!!\033[0m')
else:
    print('\033[31;1mYou LOSE!!!\033[0m')
