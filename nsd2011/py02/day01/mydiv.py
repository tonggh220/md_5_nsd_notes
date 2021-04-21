# try:
#     num = int(input('number: '))
#     result = 100 / num
#     print(result)
# except ValueError:
#     print('请输入非0数字')
# except ZeroDivisionError:
#     print('请输入非0数字')
# except KeyboardInterrupt:
#     print('\nBye-bye')
# except EOFError:
#     print('\nBye-bye')

###########################
# try:
#     num = int(input('number: '))
#     result = 100 / num
#     print(result)
# except (ValueError, ZeroDivisionError):
#     print('请输入非0数字')
# except (KeyboardInterrupt, EOFError):
#     print('\nBye-bye')

###########################
# try:
#     num = int(input('number: '))
#     result = 100 / num
# except (ValueError, ZeroDivisionError):
#     print('请输入非0整数')
# except (KeyboardInterrupt, EOFError):
#     print('\nBye-bye')
# else:  # 不发生异常才执行的语句
#     print(result)
#
# print('ok')


# ###########################
# try:
#     num = int(input('number: '))
#     result = 100 / num
# except (ValueError, ZeroDivisionError):
#     print('请输入非0整数')
# except (KeyboardInterrupt, EOFError):
#     print('\nBye-bye')
#     exit()  # 程序遇到exit时，彻底结束
# else:  # 不发生异常才执行的语句
#     print(result)
#
# print('ok')


###########################
try:
    num = int(input('number: '))
    result = 100 / num
except (ValueError, ZeroDivisionError):
    print('请输入非0整数')
except (KeyboardInterrupt, EOFError):
    print('\nBye-bye')
    exit()  # 程序遇到exit时，彻底结束
else:  # 不发生异常才执行的语句
    print(result)
finally:  # 不管异常是否发生，都要执行的语句
    print('ok')
