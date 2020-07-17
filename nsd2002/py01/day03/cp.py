# 代码需要改进的地方
# 1. 不建议直接使用字面量，应该使用变量
# 2. 变量名应该有意义
# 3. 一次将所有数据读出，可能数据量太大
f1 = open('/tmp/girl.jpg', 'rb')
f2 = open('/var/tmp/girl.jpg', 'wb')

data = f1.read()
f2.write(data)

f1.close()
f2.close()

# md5sum /tmp/girl.jpg /var/tmp/girl.jpg
# eog /var/tmp/girl.jpg
