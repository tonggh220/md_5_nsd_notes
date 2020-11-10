import random

# 人机进行选择
all_choices = ['石头', '剪刀', '布']
win_list = [['石头', '剪刀'], ['剪刀', '布'], ['布', '石头']]  # 定义人赢的情况
computer = random.choice(all_choices)
player = input('请选择(石头/剪刀/布): ')

# 输出人机选择
print('你出了:%s, 计算机出:%s' % (player, computer))

# 判断胜负
if player == computer:
    print('平局')
elif [player, computer] in win_list:  # 人机选择组成的小列表是大列表中的一项
    print('You WIN!!!')
else:
    print('You LOSE!!!')
