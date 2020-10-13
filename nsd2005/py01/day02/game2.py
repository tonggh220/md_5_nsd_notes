import random

# 定义人胜利的列表
win_list = [['石头', '剪刀'], ['剪刀', '布'], ['布', '石头']]

# 人机分别出拳
all_choice = ['石头', '剪刀', '布']
computer = random.choice(all_choice)
player = input("请出拳(石头/剪刀/布): ")

# 打印人机选择
print("计算机的选择:%s, 您的选择:%s" % (computer, player))

# 判断并输出胜负
if computer == player:
    print("平局")
elif [player, computer] in win_list:
    print("You WIN!!!")
else:
    print("You LOSE!!!")
