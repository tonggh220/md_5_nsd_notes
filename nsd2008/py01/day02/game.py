import random

# 定义计算机可以选择的列表
all_choices = ['石头', '剪刀', '布']

# 人机分别出拳
player = input("请出拳(石头/剪刀/布): ")
computer = random.choice(all_choices)

# 输出人机选择
# print("Your choice:", player, ", Computer's choice:", computer)
print("Your choice: %s, Computer's choice: %s" % (player, computer))

# 判断胜负
if player == "石头":
    if computer == "石头":
        print("平局")
    elif computer == "剪刀":
        print("You WIN!!!")
    else:
        print("You LOSE!!!")
elif player == "剪刀":
    if computer == "石头":
        print("You LOSE!!!")
    elif computer == "剪刀":
        print("平局")
    else:
        print("You WIN!!!")
else:
    if computer == "石头":
        print("You WIN!!!")
    elif computer == "剪刀":
        print("You LOSE!!!")
    else:
        print("平局")
