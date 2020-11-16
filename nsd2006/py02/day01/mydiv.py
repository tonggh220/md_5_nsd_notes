try:
    num = int(input("number: "))
    result = 100 / num
    print(result)
    print('Done')
except ValueError:
    print("请输入非0输字")
except ZeroDivisionError:
    print("请输入非0输字")
except KeyboardInterrupt:
    print("\nBye-bye")
except EOFError:
    print("\nBye-bye")
