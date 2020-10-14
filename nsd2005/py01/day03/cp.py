# 代码问题:
# 1. 多用变量，而不是字面量
# 2. 变量名应该有意义
# 3. 如果源文件太大，将会占用太多的内存资源


# 打开两个文件
f1 = open('/bin/ls', 'rb')
f2 = open('/tmp/ls', 'wb')

# 将数据从源文件中取出，写入到目标文件
data = f1.read()
f2.write(data)

# 关闭
f1.close()
f2.close()
