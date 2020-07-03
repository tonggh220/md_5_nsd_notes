import os
import wget
import re

def get_url(fname, patt, charset=None):
    # 在文件中找到所有的模式，保存到列表
    cpatt = re.compile(patt)
    result = []
    with open(fname, encoding=charset) as fobj:
        for line in fobj:
            m = cpatt.search(line)
            if m:
                result.append(m.group())
    return result

if __name__ == '__main__':
    # 下载网易首页上全部的图片
    dest = '/tmp/163'
    fname163 = '/tmp/163/163.html'
    url163 = 'http://www.163.com'
    if not os.path.exists(dest):
        os.mkdir(dest)
    if not os.path.exists(fname163):
        wget.download(url163, fname163)

    # 获取163.html中所有图片的url
    img_patt = '(http|https)://[\w/.-]+\.(jpg|gif|png|jpeg)'
    img_list = get_url(fname163, img_patt, 'gbk')
    # print(img_list)
    for url in img_list:
        wget.download(url, dest)
