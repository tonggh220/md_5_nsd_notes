# try:
#     i = int(input('number: '))
#     result = 100 / i
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
#     i = int(input('number: '))
#     result = 100 / i
#     print(result)
#     print('Done')
# except (ValueError, ZeroDivisionError):
#     print('请输入非0数字')
# except (KeyboardInterrupt, EOFError):
#     print('\nBye-bye')


# try:
#     i = int(input('number: '))
#     result = 100 / i
# except (ValueError, ZeroDivisionError):
#     print('请输入非0数字')
# except (KeyboardInterrupt, EOFError):
#     print('\nBye-bye')
# else:
#     print(result)
#
# print('Done')


try:
    i = int(input('number: '))
    result = 100 / i
except (ValueError, ZeroDivisionError):
    print('请输入非0数字')
except (KeyboardInterrupt, EOFError):
    print('\nBye-bye')
    exit(1)
else:
    print(result)
finally:
    print('Done')
