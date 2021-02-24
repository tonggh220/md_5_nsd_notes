import os
import wget
import re

def get_patt(fname, patt, charset=None):
    cpatt = re.compile(patt)
    result = []

    with open(fname, encoding=charset) as fobj:
        for line in fobj:
            m = cpatt.search(line)
            if m:
                result.append(m.group())

    return result

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
    img_patt = '(http|https)://[\w./-]+\.(jpg|jpeg|gif|png)'
    img_list = get_patt(fname163, img_patt, 'gbk')

    # 下载图片
    for img_url in img_list:
        wget.download(img_url, dir163)
