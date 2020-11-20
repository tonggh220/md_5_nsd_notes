import os
import wget
import re

def get_patt(fname, patt, charset=None):
    result = []
    cpatt = re.compile(patt)
    with open(fname, encoding=charset) as fobj:
        for line in fobj:
            m = cpatt.search(line)
            if m:
                result.append(m.group())

    return result

if __name__ == '__main__':
    # 下载网易首页
    img_dir = '/tmp/163'
    fname163 = '/tmp/163/163.html'
    url163 = 'http://www.163.com'
    if not os.path.exists(img_dir):
        os.mkdir(img_dir)
    if not os.path.exists(fname163):
        wget.download(url163, fname163)

    # 取出网易站点上所有的图片url
    img_patt = '(http|https)://[\w./-]+\.(jpg|jpeg|png|gif)'
    img_list = get_patt(fname163, img_patt, 'gbk')

    # 下载图片
    for url in img_list:
        wget.download(url, img_dir)
