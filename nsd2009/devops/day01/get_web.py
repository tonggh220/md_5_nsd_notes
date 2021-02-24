import os
import wget


if __name__ == '__main__':
    # 下载网易首页
    dir163 = '/tmp/163'
    fname163 = '/tmp/163/163.html'
    url163 = 'http://www.163.com/'
    if not os.path.exists(dir163):
        os.mkdir(dir163)
    if not os.path.exists(fname163):
        wget.download(url163, fname163)

    # 在网易首页中找到图片地址

    # 下载图片
