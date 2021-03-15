import random

num = random.randint(1, 100)
i = 0

while i < 7:
    answer = int(input("guess: "))
    if answer > num:
        print('猜大了')
    elif answer < num:
        print('猜小了')
    else:
        print('猜对了')
        break

    i += 1
else:
    print(f'答案是: {num}')
