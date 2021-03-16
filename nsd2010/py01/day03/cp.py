# 问题：
# 1. 不建议使用字面量，应该使用变量
# 2. 变量名应该有意义
# 3. 如果一次性把数据全部读入内存，数据可量可能过大

f1 = open('/tmp/girl.jpg', 'rb')
f2 = open('/var/tmp/girl.jpg', 'wb')

data = f1.read()
f2.write(data)

f1.close()
f2.close()
