# 代码的问题:
# 1. 文件名应该定义为变量
# 2. 变量名应该有意义
# 3. 如果文件很大，data变量将会占用太多的内存
f1 = open('/bin/ls', 'rb')
f2 = open('/tmp/ls', 'wb')

data = f1.read()
f2.write(data)

f1.close()
f2.close()
