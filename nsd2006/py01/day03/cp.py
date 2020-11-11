# 当前代码问题
# 1. 不推荐直接使用字面量，而是使用变量
# 2. 应该使用有意义的变量名
# 3. 变量存在内存中，注意它的大小
f1 = open('/tmp/girl.jpg', 'rb')
f2 = open('/var/tmp/girl.jpg', 'wb')

data = f1.read()
f2.write(data)

f1.close()
f2.close()
