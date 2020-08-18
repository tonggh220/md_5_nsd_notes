# try:
#     n = int(input('number: '))
#     result = 100 / n
#     print(result)
#     print('Done')
# except ValueError:
#     print('请输入非0数字')
# except ZeroDivisionError:
#     print('请输入非0数字')
# except KeyboardInterrupt:
#     print('\nBye-bye')
# except EOFError:
#     print('\nBye-bye')

# try:
#     n = int(input('number: '))
#     result = 100 / n
#     print(result)
#     print('Done')
# except (ValueError, ZeroDivisionError):
#     print('请输入非0数字')
# except (KeyboardInterrupt, EOFError):
#     print('\nBye-bye')

# try:
#     n = int(input('number: '))
#     result = 100 / n
#     print(result)
#     print('Done')
# except (ValueError, ZeroDivisionError) as e:  # 将报错信息保存到变量e中
#     print('请输入非0数字:', e)
# except (KeyboardInterrupt, EOFError):
#     print('\nBye-bye')

try:
    n = int(input('number: '))
    result = 100 / n
except (ValueError, ZeroDivisionError) as e:  # 将报错信息保存到变量e中
    print('请输入非0数字:', e)
except (KeyboardInterrupt, EOFError):
    print('\nBye-bye')
else:
    print(result)  # 异常不发生时，才执行

print('Done')
