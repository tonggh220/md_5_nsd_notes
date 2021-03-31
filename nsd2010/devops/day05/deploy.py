import requests
import wget
import os
import hashlib
import tarfile

def has_new_ver(ver_url, ver_fname):
    '如果有新版本返回True，否则返回False'
    # 本地不存在版本文件，则有新版本
    if not os.path.exists(ver_fname):
        return True

    # 本地和网上版本不一样则有新版本，否则没有
    r = requests.get(ver_url)
    with open(ver_fname) as fobj:
        local_ver = fobj.read()

    if local_ver != r.text:
        return True
    else:
        return False


def file_ok(md5url, app_fname):
    '如果文件完好返回True，否则返回False'
    # 计算本地文件的md5值
    m = hashlib.md5()
    with open(app_fname, 'rb') as fobj:
        while 1:
            data = fobj.read(4096)
            if not data:
                break
            m.update(data)

    r = requests.get(md5url)
    if m.hexdigest() == r.text.strip():  # 去除文件结尾的\n
        return True
    else:
        return False

def deploy(app_fname, deploy_dir, dest):
    '部署软件'
    # 解压
    with tarfile.open(app_fname) as tar:
        tar.extractall(path=deploy_dir)

    # 拼接出解压目录的绝对路径
    app_dir = os.path.basename(app_fname)
    app_dir = app_dir.replace('.tar.gz', '')
    app_dir = os.path.join(deploy_dir, app_dir)

    # 如果dest已存在，则删除它
    if os.path.exists(dest):
        os.remove(dest)

    # 创建软链接
    os.symlink(app_dir, dest)

if __name__ == '__main__':
    # 判断是否有新版本，没有则退出
    ver_url = 'http://192.168.1.103/deploy/live_ver'
    ver_fname = '/var/www/deploy/live_ver'
    if not has_new_ver(ver_url, ver_fname):
        print('未发现新版本')
        exit(1)

    # 下载新版本软件包
    download_dir = '/var/www/download'
    r = requests.get(ver_url)
    app_url = f'http://192.168.1.103/deploy/pkgs/myweb-{r.text}.tar.gz'
    wget.download(app_url, download_dir)

    # 判断文件是否完好，如已损坏则删除它并退出
    md5url = app_url + '.md5'
    app_fname = app_url.split('/')[-1]
    app_fname = os.path.join(download_dir, app_fname)
    if not file_ok(md5url, app_fname):
        print('文件已损坏')
        exit(2)

    # 部署软件
    deploy_dir = '/var/www/deploy'
    dest = '/var/www/html/nsd2010'
    deploy(app_fname, deploy_dir, dest)

    # 更新本地版本
    if os.path.exists(ver_fname):
        os.remove(ver_fname)
    wget.download(ver_url, ver_fname)
