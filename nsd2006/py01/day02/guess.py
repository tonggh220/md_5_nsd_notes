import random

num = random.randint(1, 100)
i = 1

while i < 8:
    i += 1
    answer = int(input("guess: "))
    if answer > num:
        print("猜大了")
    elif answer < num:
        print("猜小了")
    else:
        print("猜对了")
        break
else:
    print("the number is:", num)
