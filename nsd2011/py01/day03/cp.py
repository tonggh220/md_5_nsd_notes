# 1. 建议使用变量，而不是字面量
# 2. 建议使用有意义的名字
# 3. 如果文件非常大，一次全部取出放到内存不可取

f1 = open('/tmp/girl.jpg', 'rb')
f2 = open('/var/tmp/g.jpg', 'wb')

data = f1.read()
f2.write(data)

f1.close()
f2.close()
