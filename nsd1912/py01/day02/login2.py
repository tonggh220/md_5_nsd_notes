import getpass   # 导入getpass模块

username = input('username: ')
password = getpass.getpass('password: ')

if username == 'bob' and password == '123456':
    print('登陆成功')
else:
    print('登陆失败')
