# python3 cp_func.py /bin/ls /tmp/list
import sys

def copy(src_fname, dst_fname):
    src_fobj = open(src_fname, 'rb')
    dst_fobj = open(dst_fname, 'wb')

    while 1:
        data = src_fobj.read(4096)  # 一次最多读取4096字节
        if not data:  # 如果data为空，表示假，取反为真; 如果data非空，表示真，取反为假
            break
        dst_fobj.write(data)

    src_fobj.close()
    dst_fobj.close()

copy(sys.argv[1], sys.argv[2])
