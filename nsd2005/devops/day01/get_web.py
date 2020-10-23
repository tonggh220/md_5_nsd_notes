import wget
import re
import os

def get_patt(fname, patt):

if __name__ == '__main__':
    # 定义下载目录
    down_dir = '/tmp/163'
    fname163 = '/tmp/163/163.html'
    url163 = 'http://www.163.com'
    if not os.path.exists(down_dir):
        os.mkdir(down_dir)
    if not os.path.exists(fname163):
        wget.download(url163, fname163)

    # 在网易首页中找到所有图片的Url
    img_patt = ''
    img_list = get_patt(fname163, img_patt)
    for url in img_list:
        wget.download(url, down_dir)
