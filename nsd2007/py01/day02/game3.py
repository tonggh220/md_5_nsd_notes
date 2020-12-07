import random

# 列出所有可用选择
all_choice = ['石头', '剪刀', '布']
# 定义人胜利的列表
win_list = [['石头', '剪刀'], ['剪刀', '布'], ['布', '石头']]
prompt = """(0) 石头
(1) 剪刀
(2) 布
请选择(0/1/2): """
computer = random.choice(all_choice)
i = int(input(prompt))
player = all_choice[i]
# 输出人机选择
print('player: %s, computer: %s' % (player, computer))
# 判断胜负
if player == computer:
    print('\033[32;1m平局\033[0m')
elif [player, computer] in win_list:
    print('\033[31;1mYou WIN!!!\033[0m')
else:
    print('\033[31;1mYou LOSE!!!\033[0m')
