try:
    num = int(input('number: '))
    result = 100 / num
    print(result)
except ValueError:
    print('请输入非0数字')
except ZeroDivisionError:
    print('请输入非0数字')
except KeyboardInterrupt:
    print('\nBye-bye')
except EOFError:
    print('\nBye-bye')
