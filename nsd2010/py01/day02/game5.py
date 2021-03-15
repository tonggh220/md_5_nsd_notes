import random

# 定义计算机随机出拳的范围
all_choices = ['石头', '剪刀', '布']
# 定义人胜利的情形
win_list = [['石头', '剪刀'], ['剪刀', '布'], ['布', '石头']]
prompt = '''(0) 石头
(1) 剪刀
(2) 布
请出拳(0/1/2): '''
cwin = 0  # 创建计算机的计分牌
pwin = 0  # 创建人的计分牌

while 1:  # 非0数字都为真
    # 计算机随机出拳
    computer = random.choice(all_choices)
    # 人出拳
    i = int(input(prompt))    # 获取用户输入的内容，转换成整数
    player = all_choices[i]   # 通过下标取出值
    # 输出人机选择
    print(f'你出了：{player}，计算机出了：{computer}')

    # 判断胜负
    if player == computer:
        print('\033[32;1m平局\033[0m')
    elif [player, computer] in win_list:
        print('\033[31;1mYou WIN!!!\033[0m')
        pwin += 1
    else:
        print('\033[31;1mYou LOSE!!!\033[0m')
        cwin += 1

    if cwin == 2 or pwin == 2:
        break  # 人机有任何一方赢够2次，则中断循环

print('Bye-bye')
