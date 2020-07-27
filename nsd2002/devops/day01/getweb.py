from urllib import request
import sys

def download(url, fname):
    html = request.urlopen(url)
    with open(fname, 'wb') as fobj:
        while 1:
            data = html.read(4096)
            if not data:
                break
            fobj.write(data)

if __name__ == '__main__':
    download(sys.argv[1], sys.argv[2])
# python3 getweb.py http://pic-bucket.ws.126.net/photo/0003/2020-07-26/FIG0JHVE00AJ0003NOS.jpg /tmp/zhao.jpg
# [root@localhost day01]# eog /tmp/zhao.jpg
