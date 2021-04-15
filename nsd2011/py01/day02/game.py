import random

all_choice = ['石头', '剪刀', '布']
# 计算机随机出拳
computer = random.choice(all_choice)
# 人出拳
player = input('请出拳(石头/剪刀/布): ')

# 输出人机的选择, 字符串加上前缀f，可以在字符串中使用{}来书写变量
print(f'计算机出拳:{computer}, 你出拳:{player}')
# 判断胜负，并输出结果
if player == '石头':
    if computer == '石头':
        print('\033[32;1m平局\033[0m')
    elif computer == '剪刀':
        print('\033[31;1mYou WIN!!!\033[0m')
    else:
        print('\033[31;1mYou LOSE!!!\033[0m')
elif player == '剪刀':
    if computer == '石头':
        print('\033[31;1mYou LOSE!!!\033[0m')
    elif computer == '剪刀':
        print('\033[32;1m平局\033[0m')
    else:
        print('\033[31;1mYou WIN!!!\033[0m')
else:
    if computer == '石头':
        print('\033[31;1mYou WIN!!!\033[0m')
    elif computer == '剪刀':
        print('\033[31;1mYou LOSE!!!\033[0m')
    else:
        print('\033[32;1m平局\033[0m')
