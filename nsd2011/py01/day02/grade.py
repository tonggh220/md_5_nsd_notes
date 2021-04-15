score = input('分数: ')
score = int(score)  # 将字符串‘10’转成数字10再赋值给score变量

if score >= 90:
    print('优秀')
elif score >= 80:
    print('好')
elif score >= 70:
    print('良')
elif score >= 60:
    print('及格')
else:
    print('你要努力了!!!')
