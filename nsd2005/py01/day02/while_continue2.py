result = 0
i = 0

while i < 100:
    i += 1
    if i % 2:  # i%2的结果只有1或0，1为真，0为假
        continue
    result += i

print(result)
