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
    # 定义保存图片目录。下载网易首页
    url = 'http://www.163.com'
    img_dir = '/tmp/163'
    fname = '/tmp/163/163.html'
    if not os.path.exists(img_dir):
        os.mkdir(img_dir)
    if not os.path.exists(fname):
        wget.download(url, fname)

    # 在网易首页文件中找到所有图片的URL
    img_patt = '(http|https)://[\w/.-]+\.(jpg|jpeg|png|gif)'
    img_list = get_patt(fname, img_patt, 'gbk')

    # 下载图片
    for url in img_list:
        wget.download(url, img_dir)
