import sys

def copy(src_fname, dst_fname):
    src_fobj = open(src_fname, 'rb')
    dst_fobj = open(dst_fname, 'wb')

    while 1:
        data = src_fobj.read(4096)
        if not data:  # data为空时表示假，取反为真；data非空时为真，取反为假
            break
        dst_fobj.write(data)

    src_fobj.close()
    dst_fobj.close()

if __name__ == '__main__':
    copy(sys.argv[1], sys.argv[2])
