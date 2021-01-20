import os
import wget
import re

def get_patt(fname, patt, charset=None):
    "在文件fname中，找到给定的patt"
    cpatt = re.compile(patt)
    result = []
    with open(fname, encoding=charset) as fobj:
        for line in fobj:
            m = cpatt.search(line)
            if m:
                result.append(m.group())
    return result


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
    img_patt = '(http|https)://[\w/.-]+\.(jpg|jpeg|png|gif)'
    # 检查网易首页文件最上面的几行，发现它用的字符编码是gbk
    # 所以打开文件时要添加encoding='gbk'
    img_list = get_patt(fname163, img_patt, 'gbk')

    # 下载图片
    for img_url in img_list:
        wget.download(img_url, dst)
