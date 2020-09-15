try:
    n = int(input('number: '))
    result = 100 / n
    print(result)
    print('Done')
except ValueError:
    print('请输入非0数字')
