import random

num = random.randint(1, 100)
i = 0

while i < 7:
    answer = int(input("guess the number: "))
    if answer == num:
        print('猜对了')
        break
    if answer > num:
        print('猜大了')
    else:
        print('猜小了')
    i += 1
else:
    print("the number is:", num)
