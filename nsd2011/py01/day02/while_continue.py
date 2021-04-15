# 计算1到100之间偶数的和

# 首先定义用于保存结果的变量
result = 0
# 定义用于累加的变量
i = 0

while i < 100:
    i += 1
    if i % 2 == 1:
        continue
    else:
        result += i

print(result)
