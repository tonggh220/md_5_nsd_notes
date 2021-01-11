import random

# 定义计算机可以选择的列表
all_choices = ['石头', '剪刀', '布']
# 人的选择在前，定义人可以胜利的情况
win_list = [['石头', '剪刀'], ['剪刀', '布'], ['布', '石头']]
# 把input函数中的提示字符串定义成一个变量
prompt = """(0) 石头
(1) 剪刀
(2) 布
请选择(0/1/2): """

# 为人机分别创建计分牌
pwin = 0
cwin = 0

while 1:  # 循环条件永远为真
    # 人机分别出拳
    i = int(input(prompt))   # 将用户输入的字符转成数字
    player = all_choices[i]  # 通过下标将输入转换成石头剪刀布
    computer = random.choice(all_choices)

    # 输出人机选择
    print("Your choice: %s, Computer's choice: %s" % (player, computer))

    # 判断胜负
    if player == computer:
        print("\033[32;1m平局\033[0m")
    elif [player, computer] in win_list:
        # 人机的选择，构成列表，正好是win_list列表中的一项
        pwin += 1
        print("\033[31;1mYou WIN!!!\033[0m")
    else:
        cwin += 1
        print("\033[31;1mYou LOSE!!!\033[0m")

    if pwin == 2 or cwin == 2:
        break
