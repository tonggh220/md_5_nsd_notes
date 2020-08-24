from urllib import request
import sys

def download(url, dest):
    html = request.urlopen(url)
    with open(dest, 'wb') as fobj:
        while 1:
            data = html.read(4096)
            if not data:
                break
            fobj.write(data)

if __name__ == '__main__':
    download(sys.argv[1], sys.argv[2])
# python3 download.py http://pic1.win4000.com/wallpaper/a/5870bc412f3be.jpg /tmp/girl.jpg
# eog /tmp/girl.jpg
