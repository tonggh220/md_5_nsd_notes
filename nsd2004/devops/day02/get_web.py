import os
import wget

def get_patt(fname, patt):

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
    img_patt = ''
    img_list = get_patt(fname, img_patt)

    # 下载图片
    for url in img_list:
        wget.download(url, img_dir)
