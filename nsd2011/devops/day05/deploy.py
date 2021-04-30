import requests
import wget
import os
import hashlib

def has_new_ver(ver_url, ver_fname):
    '判断是否有新版本，有新版本返回True，否则返回False'
    # 本地不存在版本文件，则有新版本
    if not os.path.isfile(ver_fname):
        return True

    # 本地和网上版本不一样，则有新版本
    with open(ver_fname) as fobj:
        local_ver = fobj.read()

    r = requests.get(ver_url)
    if local_ver != r.text:
        return True
    else:
        return False

def file_ok(md5url, app_fname):
    '判断文件是否完好，完好返回True，否则返回False'
    # 计算本地文件md5值
    m = hashlib.md5()

    with open(app_fname, 'rb') as fobj:
        while 1:
            data = fobj.read(4096)
            if not data:
                break
            m.update(data)

    # 取出网上md5值，并进行比较
    r = requests.get(md5url)
    if m.hexdigest() == r.text.strip():  # 删除结尾的\n
        return True
    else:
        return False

def deploy(app_fname, deploy_dir, dest):
    '用于部署软件'

if __name__ == '__main__':
    # 判断是否有新版本，没有新版本则退出
    ver_url = 'http://192.168.1.103/deploy/live_ver'
    ver_fname = '/var/www/deploy/live_ver'
    if not has_new_ver(ver_url, ver_fname):
        print('未发现新版本')
        exit(1)

    # 下载新版本软件
    download_dir = '/var/www/download'
    r = requests.get(ver_url)
    app_url = f'http://192.168.1.103/deploy/pkgs/myweb-{r.text}.tar.gz'
    wget.download(app_url, download_dir)

    # 判断文件是否损坏，如已损坏则删除它并退出
    md5url = app_url + '.md5'
    app_fname = app_url.split('/')[-1]
    app_fname = os.path.join(download_dir, app_fname)
    if not file_ok(app_url, app_fname):
        print('文件已损坏')
        os.remove(app_fname)
        exit(2)

    # 部署软件
    deploy_dir = '/var/www/deploy'
    dest = '/var/www/html/nsd2011'
    deploy(app_fname, deploy_dir, dest)

    # 更新本地版本
    if os.path.exists(ver_fname):
        os.remove(ver_fname)
    wget.download(ver_url, ver_fname)
