import random

# 定义计算机可以选择的列表
all_choices = ['石头', '剪刀', '布']
# 人的选择在前，定义人可以胜利的情况
win_list = [['石头', '剪刀'], ['剪刀', '布'], ['布', '石头']]

# 人机分别出拳
player = input("请出拳(石头/剪刀/布): ")
computer = random.choice(all_choices)

# 输出人机选择
print("Your choice: %s, Computer's choice: %s" % (player, computer))

# 判断胜负
if player == computer:
    print("平局")
elif [player, computer] in win_list:
    # 人机的选择，构成列表，正好是win_list列表中的一项
    print("You WIN!!!")
else:
    print("You LOSE!!!")
