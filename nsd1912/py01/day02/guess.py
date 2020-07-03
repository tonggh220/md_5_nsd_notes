import random

n = random.randint(1, 100)
i = 0

while i < 7:
    answer = int(input('guess(1-100): '))
    if answer > n:
        print('猜大了')
    elif answer < n:
        print('猜小了')
    else:
        print('猜对了')
        break
    i += 1
else:
    print('答案是:%s' % n)
