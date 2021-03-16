src_fname = '/tmp/girl.jpg'
dst_fname = '/tmp/girl2.jpg'

src_fobj = open(src_fname, 'rb')
dst_fobj = open(dst_fname, 'wb')

while 1:
    data = src_fobj.read(4096)  # 从源文件中最多读取4096字节
    if not data:  # 任何空对象都是假，非空为真
        break
    dst_fobj.write(data)

src_fobj.close()
dst_fobj.close()
