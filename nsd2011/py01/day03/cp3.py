src_fname = '/tmp/girl.jpg'   # 源文件名
dst_fname = '/var/tmp/g.jpg'  # 目标文件名

src_fobj = open(src_fname, 'rb')
dst_fobj = open(dst_fname, 'wb')

while 1:
    data = src_fobj.read(4096)  # 最多读取4096字节数据
    if not data:  # data非空为真，取反为假；data是空的为假，取反为真
        break
    dst_fobj.write(data)

src_fobj.close()
dst_fobj.close()
