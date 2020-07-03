f1 = open('/root/girl.jpg', 'rb')
f2 = open('/tmp/g.jpg', 'wb')

data = f1.read()
f2.write(data)

f1.close()
f2.close()

# 分析，代码需要改进的地方
# 1. 建议使用变量，而不是硬编码。文件名应该使用变量
# 2. 变量名应该有意义，而不是简单的f1/f2
# 3. 一次将文件所有内容读取出来，如果文件较大，将会占用太多的内存
