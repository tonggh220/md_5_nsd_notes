import wget
import os
import re
from urllib import error

def get_patt(fname, patt, charset='utf8'):
    cpatt = re.compile(patt)
    patt_list = []
    with open(fname, encoding=charset) as fobj:
        for line in fobj:
            m = cpatt.search(line)
            if m:
                patt_list.append(m.group())
    return patt_list

if __name__ == '__main__':
    fname = '/tmp/163/163.html'
    url_163 = 'http://www.163.com'
    img_dir = '/tmp/163'
    # 如果目录不存在，则创建；如果文件不存在，则下载
    if not os.path.exists(img_dir):
        os.mkdir(img_dir)
    if not os.path.exists(fname):
        wget.download(url_163, fname)

    # 遍历文件，取出文件中图片的url
    img_patt = '(http|https)://[\w./-]+\.(jpg|jpeg|png|gif)'
    img_list = get_patt(fname, img_patt, 'gbk')
    # print(img_list)
    # 下载图片
    for img_url in img_list:
        try:
            wget.download(img_url, img_dir)
        except error.HTTPError:
            pass
