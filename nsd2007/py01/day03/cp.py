# 存在的问题：
# 1. 不建议直接使用字面量，而是使用变量
# 2. 变量名应该有意义
# 3. 读取文件内容时，不应该一次把全部数据全读取出来，因为文件可能过大
f1 = open('/tmp/girl.jpg', 'rb')
f2 = open('/var/tmp/ggg.jpg', 'wb')

data = f1.read()
f2.write(data)

f1.close()
f2.close()
