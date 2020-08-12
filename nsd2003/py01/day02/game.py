import random

# 定义所有可用的选择
all_choice = ['石头', '剪刀', '布']

# 人机分别出拳
computer = random.choice(all_choice)
player = input('请出拳(石头/剪刀/布): ')

# 输出人机选择
print('计算机出了:%s，你出了:%s' % (computer, player))

# 判断输赢
if player == '石头':
    if computer == '石头':
        print('平局')
    elif computer == '剪刀':
        print('You WIN!!!')
    else:
        print('You LOSE!!!')
elif player == '剪刀':
    if computer == '石头':
        print('You LOSE!!!')
    elif computer == '剪刀':
        print('平局')
    else:
        print('You WIN!!!')
else:
    if computer == '石头':
        print('You WIN!!!')
    elif computer == '剪刀':
        print('You LOSE!!!')
    else:
        print('平局')
