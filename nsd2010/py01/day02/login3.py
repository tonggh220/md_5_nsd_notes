# python有很多功能，这些功能被分门别类放到了不同的模块中，要使用相关的功能，必须将其模块导入\
# 一个模块可以有很多功能。使用模块功能时，采用 模块.属性 的方式
import getpass

username = input('username: ')
password = getpass.getpass('password: ')
if username == 'bob' and password == '123456':
    print('Login Successful')
else:
    print('Login Failed')
