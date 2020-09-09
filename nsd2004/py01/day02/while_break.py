# 猜数，1到100以内的数字
import random

result = random.randint(1, 100)
i = 0

while i < 7:
    i += 1
    answer = int(input('guess the number: '))
    if answer > result:
        print('猜大了')
    elif answer < result:
        print('猜小了')
    else:
        print('猜对了')
        break
else:  # 循环被break掉，else语句不执行，否则执行
    print('the answer: %s' % result)
