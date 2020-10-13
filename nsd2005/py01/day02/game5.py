import random

# 定义人胜利的列表
win_list = [['石头', '剪刀'], ['剪刀', '布'], ['布', '石头']]

# 人机分别出拳
all_choice = ['石头', '剪刀', '布']
prompt = """(0) 石头
(1) 剪刀
(2) 布
请选择(0/1/2): """
# 定义人机胜利计数器
pwin = 0
cwin = 0

while 1:
    computer = random.choice(all_choice)
    ind = int(input(prompt))
    player = all_choice[ind]

    # 打印人机选择
    print("计算机的选择:%s, 您的选择:%s" % (computer, player))

    # 判断并输出胜负
    if computer == player:
        print("\033[32;1m平局\033[0m")
    elif [player, computer] in win_list:
        pwin += 1
        print("\033[31;1mYou WIN!!!\033[0m")
    else:
        cwin += 1
        print("\033[31;1mYou LOSE!!!\033[0m")

    if pwin == 2 or cwin == 2:
        break
