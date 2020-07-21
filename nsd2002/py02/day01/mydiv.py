# try:
#     n = int(input('number: '))
#     result = 100 / n
#     print(result)
#     print('Done')
# except ValueError:
#     print('只接受非0数字')
# except ZeroDivisionError:
#     print('只接受非0数字')
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
#     print('只接受非0数字')
# except (KeyboardInterrupt, EOFError):
#     print('\nBye-bye')

try:
    n = int(input('number: '))
    result = 100 / n
    print(result)
    print('Done')
except (ValueError, ZeroDivisionError) as e:  # 将异常保存为变量e
    print('只接受非0数字: ', e)
except (KeyboardInterrupt, EOFError):
    print('\nBye-bye')
