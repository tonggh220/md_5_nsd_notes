# try:
#     num = int(input("number: "))
#     result = 100 / num
#     print(result)
#     print('Done')
# except ValueError:
#     print("请输入非0输字")
# except ZeroDivisionError:
#     print("请输入非0输字")
# except KeyboardInterrupt:
#     print("\nBye-bye")
# except EOFError:
#     print("\nBye-bye")

# try:
#     num = int(input("number: "))
#     result = 100 / num
#     print(result)
#     print('Done')
# except (ValueError, ZeroDivisionError):
#     print("请输入非0输字")
# except (KeyboardInterrupt, EOFError):
#     print("\nBye-bye")

# try:
#     num = int(input("number: "))
#     result = 100 / num
#     print(result)
#     print('Done')
# except (ValueError, ZeroDivisionError) as e:  # 将异常保存到变量e
#     print("请输入非0输字:", e)
# except (KeyboardInterrupt, EOFError):
#     print("\nBye-bye")

# try:
#     num = int(input("number: "))
#     result = 100 / num
# except (ValueError, ZeroDivisionError) as e:  # 将异常保存到变量e
#     print("请输入非0输字:", e)
# except (KeyboardInterrupt, EOFError):
#     print("\nBye-bye")
# else:
#     print(result)
#
# print('Done')

# try:
#     num = int(input("number: "))
#     result = 100 / num
# except (ValueError, ZeroDivisionError) as e:  # 将异常保存到变量e
#     print("请输入非0输字:", e)
# except (KeyboardInterrupt, EOFError):
#     print("\nBye-bye")
#     exit(1)
# else:
#     print(result)
#
# print('Done')

try:
    num = int(input("number: "))
    result = 100 / num
except (ValueError, ZeroDivisionError) as e:  # 将异常保存到变量e
    print("请输入非0输字:", e)
except (KeyboardInterrupt, EOFError):
    print("\nBye-bye")
    exit(1)
else:
    print(result)
finally:
    print('Done')
