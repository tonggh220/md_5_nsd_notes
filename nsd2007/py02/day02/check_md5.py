import sys
import hashlib

def check_md5(fname):
    "接收文件名，返回md5值"
    m = hashlib.md5()
    with open(fname, 'rb') as fobj:
        while 1:
            data = fobj.read(4096)
            if not data:
                break
            m.update(data)

    return m.hexdigest()

if __name__ == '__main__':
    print(check_md5(sys.argv[1]))
