# 以下代码的问题
# 1. 文件名应该定义成变量
# 2. 变量名应该使用有意义的名字
# 3. 如果文件非常大，data变量将会占用太多内存

f1 = open('/tmp/ascii.png', 'rb')
f2 = open('/var/tmp/ascii.png', 'wb')

data = f1.read()
f2.write(data)

f1.close()
f2.close()
