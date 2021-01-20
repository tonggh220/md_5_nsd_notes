import os
import wget

def get_patt(fname, patt):
    "在文件fname中，找到给定的patt"


if __name__ == '__main__':
    # 创建下载目录，下载网易首页
    dst = '/tmp/163'
    fname163 = '/tmp/163/163.html'
    url163 = 'http://www.163.com'
    if not os.path.exists(dst):
        os.mkdir(dst)
    if not os.path.exists(fname163):
        wget.download(url163, fname163)

    # 在网易的首页文件中取出所有图片url
    img_patt = ''
    img_list = get_patt(fname163, img_patt)

    # 下载图片
    for img_url in img_list:
        wget.download(img_url, dst)
