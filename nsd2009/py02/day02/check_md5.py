import sys
import hashlib

def check_md5(fname):
    m = hashlib.md5()
    with open(fname, 'rb') as fobj:
        while 1:
            data = fobj.read(4096)
            if not data:
                break
            m.update(data)
    return m.hexdigest()

if __name__ == '__main__':
    fname = sys.argv[1]
    print(check_md5(fname))
