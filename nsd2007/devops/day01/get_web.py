import os
import wget

def get_patt(fname, patt):
    "在文件中找到所有模式字符串，返回列表"


if __name__ == '__main__':
    dest = '/tmp/163'
    fname163 = '/tmp/163/163.html'
    url163 = 'http://www.163.com'
    # 如果本地目录和网易首页文件不存在，则下载
    if not os.path.exists(dest):
        os.mkdir(dest)
    if not os.path.exists(fname163):
        wget.download(url163, fname163)

    # 取出网易首页文件中所有图片的url
    img_patt = ''
    img_list = get_patt(fname163, img_patt)

    # 把img_list中的每个图片下载下来
    for img_url in img_list:
        wget.download(img_url, dest)

