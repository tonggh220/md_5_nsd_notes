import random

all_choices = ['石头', '剪刀', '布']
# 计算机随机出拳
computer = random.choice(all_choices)
# 人出拳
player = input('请出拳(石头/剪刀/布): ')
# 输出人机选择
print(f'你出了：{player}，计算机出了：{computer}')

# 判断胜负
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
