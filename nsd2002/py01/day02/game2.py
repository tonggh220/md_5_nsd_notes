import random

# 定义人取胜的情况
win_list = [['石头', '剪刀'], ['剪刀', '布'], ['布', '石头']]

# 计算机随机出拳
xuan_xiang = ['石头', '剪刀', '布']
computer = random.choice(xuan_xiang)

# 人出拳
player = input('请出拳(石头/剪刀/布): ')

# 判断输赢
print('player: %s, computer: %s' % (player, computer))
if player == computer:
    print('平局')
# 人机的选择组成列表，如果正好是win_list中的一项，则人赢
elif [player, computer] in win_list:
    print('You WIN!!!')
else:
    print('You LOSE!!!')
