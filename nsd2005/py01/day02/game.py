import random

# 人机分别出拳
all_choice = ['石头', '剪刀', '布']
computer = random.choice(all_choice)
player = input("请出拳(石头/剪刀/布): ")

# 打印人机选择
print("计算机的选择:%s, 您的选择:%s" % (computer, player))

# 判断并输出胜负
if computer == "石头":
    if player == "石头":
        print("平局")
    elif player == "剪刀":
        print("You LOSE!!!")
    else:
        print("You WIN!!!")
elif computer == "剪刀":
    if player == "石头":
        print("You WIN!!!")
    elif player == "剪刀":
        print("平局")
    else:
        print("You LOSE!!!")
else:
    if player == "石头":
        print("You LOSE!!!")
    elif player == "剪刀":
        print("You WIN!!!")
    else:
        print("平局")
