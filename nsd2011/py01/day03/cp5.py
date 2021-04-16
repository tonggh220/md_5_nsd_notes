import sys

def copy(src_fname, dst_fname):
    with open(src_fname, 'rb') as src_fobj:
        with open(dst_fname, 'wb') as dst_fobj:
            while 1:
                data = src_fobj.read(4096)  # 最多读取4096字节数据
                if not data:  # data非空为真，取反为假；data是空的为假，取反为真
                    break
                dst_fobj.write(data)

copy(sys.argv[1], sys.argv[2])
# copy('/tmp/passwd', '/var/tmp/mima')
