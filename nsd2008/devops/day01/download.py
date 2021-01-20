import sys
from urllib import request

def download(url, dst):
    src = request.urlopen(url)
    with open(dst, 'wb') as fobj:
        while 1:
            data = src.read(4096)
            if not data:
                break
            fobj.write(data)

if __name__ == '__main__':
    url = sys.argv[1]
    dst = sys.argv[2]
    download(url, dst)
