# xuan_xiang = ['石头', '剪刀', '布']
# player = input("请出拳(石头/剪刀/布): ")
#
# while player not in xuan_xiang:
#     print('输入有误，请重试。')
#     player = input("请出拳(石头/剪刀/布): ")
#
# print(player)


# DRY: Don't Repeat Yourself
xuan_xiang = ['石头', '剪刀', '布']

while 1:
    player = input("请出拳(石头/剪刀/布): ")
    if player in xuan_xiang:
        break
    print('输入有误，请重试。')

print(player)
