# 1. 不建议直接用字面量(/tmp/girl.jpg)，应该用变量来表示
# 2. 变量应该使用有意义的名字
# 3. 一次性把文件所有内容都读取出来，存入变量，是存到内存。
#    文件太大，程序无法正常工作

f1 = open('/tmp/girl.jpg', 'rb')
f2 = open('/var/tmp/girl.jpg', 'wb')

data = f1.read()
f2.write(data)

f1.close()
f2.close()
# md5sum /tmp/girl.jpg /var/tmp/girl.jpg
# eog /var/tmp/girl.jpg
