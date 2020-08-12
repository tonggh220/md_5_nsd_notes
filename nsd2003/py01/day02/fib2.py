# 定义用于保存结果的变量
result = [0, 1]

l = int(input('长度: '))

for i in range(l - 2):
    result.append(result[-1] + result[-2])

print(result)
