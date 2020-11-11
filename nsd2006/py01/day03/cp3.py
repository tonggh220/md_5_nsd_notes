src_fname = '/tmp/girl.jpg'
dst_fname = '/tmp/g.jpg'

src_fobj = open(src_fname, 'rb')
dst_fobj = open(dst_fname, 'wb')

while 1:
    data = src_fobj.read(4096)
    if not data:
        break
    dst_fobj.write(data)

src_fobj.close()
dst_fobj.close()
