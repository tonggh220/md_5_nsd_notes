import random

# 定义计算机随机出拳的范围
all_choices = ['石头', '剪刀', '布']
# 定义人胜利的情形
win_list = [['石头', '剪刀'], ['剪刀', '布'], ['布', '石头']]
# 计算机随机出拳
computer = random.choice(all_choices)
# 人出拳
player = input('请出拳(石头/剪刀/布): ')
# 输出人机选择
print(f'你出了：{player}，计算机出了：{computer}')

# 判断胜负
if player == computer:
    print('\033[32;1m平局\033[0m')
elif [player, computer] in win_list:
    print('\033[31;1mYou WIN!!!\033[0m')
else:
    print('\033[31;1mYou LOSE!!!\033[0m')
