import wget
import os

def get_patt(fname, patt):

if __name__ == '__main__':
    url163 = 'http://www.163.com'
    dir163 = '/tmp/163'
    fname163 = '/tmp/163/163.html'
    # 如果本路径不存在则创建
    if not os.path.exists(dir163):
        os.mkdir(dir163)
    # 如果本地不存在网易首页文件，则下载它
    if not os.path.exists(fname163):
        wget.download(url163, fname163)

    # 在网易首页文件中取出全部的图片url
    img_patt = ''
    img_urls = get_patt(fname163, img_patt)

    # 下载图片
    for url in img_urls:
        wget.download(url, dir163)
