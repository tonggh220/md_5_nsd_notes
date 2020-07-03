src_fname = '/root/girl.jpg'
dst_fname = '/tmp/gg.jpg'

src_fobj = open(src_fname, 'rb')
dst_fobj = open(dst_fname, 'wb')

while 1:
    data = src_fobj.read(4096)  # 最多读4096字节
    # if data == b'':
    # if len(data) == 0:
    if not data:
        break

    dst_fobj.write(data)

src_fobj.close()
dst_fobj.close()
