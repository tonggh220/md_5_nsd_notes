import os
import wget
import re

def get_url(fname, patt, charset=None):
    patt_list = []
    cpatt = re.compile(patt)

    with open(fname, encoding=charset) as fobj:
        for line in fobj:
            m = cpatt.search(line)
            if m:
                patt_list.append(m.group())

    return patt_list


if __name__ == '__main__':
    # 创建下载目录，下载网易首页
    dir163 = '/tmp/163'
    fname163 = '/tmp/163/163.html'
    url163 = 'http://www.163.com'
    if not os.path.exists(dir163):
        os.mkdir(dir163)
    if not os.path.exists(fname163):
        wget.download(url163, fname163)

    # 在网易首页文件中找到所有图片的url
    img_patt = '(http|https)://[\w./-]+\.(jpg|jpeg|gif|png)'  # 图片网址的正则表达式
    img_list = get_url(fname163, img_patt, 'gbk')

    # 下载图片
    for img_url in img_list:
        try:
            wget.download(img_url, dir163)
        except:
            pass
