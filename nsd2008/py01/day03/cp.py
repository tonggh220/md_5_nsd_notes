# 1. 建议用变量，而不是真接使用字面量
# 2. 变量名应该有意义
# 3. 如果文件太大，一次性全读取出来，存到变量中是不合适的

f1 = open('/tmp/girl.jpg', 'rb')
f2 = open('/var/tmp/girl.jpg', 'wb')

data = f1.read()
f2.write(data)

f1.close()
f2.close()
