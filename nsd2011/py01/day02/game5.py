import random

all_choice = ['石头', '剪刀', '布']
win_list = [['石头', '剪刀'], ['剪刀', '布'], ['布', '石头']]
prompt = '''(0) 石头
(1) 剪刀
(2) 布
请选择(0/1/2): '''
pwin = 0  # 玩家的计分牌
cwin = 0  # 计算机的计分牌

while 1:  # 非0数字都为真
    computer = random.choice(all_choice)
    i = int(input(prompt))   # 获取用户输入的数字
    player = all_choice[i]   # 根据下标取出对应的值
    # 输出人机的选择, 字符串加上前缀f，可以在字符串中使用{}来书写变量
    print(f'计算机出拳:{computer}, 你出拳:{player}')

    if player == computer:
        print('\033[32;1m平局\033[0m')
    elif [player, computer] in win_list:
        pwin += 1
        print('\033[31;1mYou WIN!!!\033[0m')
    else:
        cwin += 1
        print('\033[31;1mYou LOSE!!!\033[0m')

    if pwin == 2 or cwin == 2:  # 人机有一方胜利2次，则结束循环
        break
