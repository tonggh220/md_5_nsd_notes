# 计算100以内偶数之和
# 定义用于保存结果的变量
result = 0
# 定义计数器，将偶数累加到变量result中
i = 0

while i < 100:
    i += 1
    if i % 2 == 1:
        continue
    else:
        result += i

print(result)
