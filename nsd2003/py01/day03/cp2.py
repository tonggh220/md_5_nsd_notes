src_fname = '/tmp/ascii.png'
dst_fname = '/var/tmp/code.png'

src_fobj = open(src_fname, 'rb')
dst_fobj = open(dst_fname, 'wb')

while 1:
    data = src_fobj.read(4096)  # 一次最多读4096字节
    if data == b'':
        break
    dst_fobj.write(data)

src_fobj.close()
dst_fobj.close()
