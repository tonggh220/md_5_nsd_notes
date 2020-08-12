import random

num = random.randint(1, 100)  # 随机生成1～100间的整数
i = 0

while i < 7:
    answer = int(input('number: '))
    if answer > num:
        print('猜大了')
    elif answer < num:
        print('猜小了')
    else:
        print('猜对了')
        break
    i += 1
else:
    print('正确答案是:', num)
