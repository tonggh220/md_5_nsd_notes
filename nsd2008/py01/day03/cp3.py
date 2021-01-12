src_fname = '/tmp/girl.jpg'
dst_fname = '/var/tmp/girl2.jpg'

src_fobj = open(src_fname, 'rb')
dst_fobj = open(dst_fname, 'wb')

while 1:
    data = src_fobj.read(4096)  # 一次最多读4096字节
    # 如果data非空，为真，取反为假；
    # 如果data是空，为假，取反为真
    if not data:
        break
    dst_fobj.write(data)

src_fobj.close()
dst_fobj.close()
