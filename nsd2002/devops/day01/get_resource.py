import os
import wget
import re

def get_patt(fname, patt, charset=None):
    cpatt = re.compile(patt)
    patt_list = []
    with open(fname, encoding=charset) as fobj:
        for line in fobj:
            m = cpatt.search(line)
            if m:
                patt_list.append(m.group())
    return patt_list

if __name__ == '__main__':
    url163 = 'http://www.163.com'
    dest = '/tmp/163'
    fname163 = '/tmp/163/163.html'
    if not os.path.exists(dest):
        os.makedirs(dest)
    # 下载网易首页文件
    if not os.path.exists(fname163):
        wget.download(url163, fname163)

    # 在网易首页文件中找出所有图片的url
    img_patt = '(http|https)://[\w/.-]+\.(jpg|jpeg|gif|png)'
    img_list = get_patt(fname163, img_patt, 'gbk')

    for img_url in img_list:
        wget.download(img_url, dest)
