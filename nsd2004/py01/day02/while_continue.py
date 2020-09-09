# 1到100以内偶数之和

# 创建一个变量，用于保存累加的结果
result = 0
# 创建一个计数器
i = 0

while i < 100:
    i += 1

    if i % 2 == 1:
        continue
    else:
        result += i

print(result)
