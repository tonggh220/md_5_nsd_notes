# 定义用于保存结果的变量
result = [0, 1]

for i in range(8):
    result.append(result[-1] + result[-2])

print(result)
