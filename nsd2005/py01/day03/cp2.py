src_fname = '/tmp/girl.jpg'
dst_fname = '/var/tmp/girl.jpg'

src_fobj = open(src_fname, 'rb')
dst_fobj = open(dst_fname, 'wb')

while 1:
    data = src_fobj.read(4096)
    if data == b'':
        break
    else:
        dst_fobj.write(data)

src_fobj.close()
dst_fobj.close()
