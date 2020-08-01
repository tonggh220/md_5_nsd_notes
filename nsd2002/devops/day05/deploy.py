import os
import requests
import wget
import hashlib
import tarfile


def has_new_ver(ver_url, ver_fname):
    "判断是否有新版本，有返回True，否则为False"
    # 本地不存在版本文件，则有新版本
    if not os.path.isfile(ver_fname):
        return True

    # 如果本地版本和网上版本不一样，则有新版本
    with open(ver_fname) as fobj:
        local_ver = fobj.read()

    r = requests.get(ver_url)
    if local_ver != r.text:
        return True
    else:
        return False


def file_ok(md5url, app_fname):
    "判断文件是否完好，完好返回True，否则为False"
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
    "部署软件"
    # 解压
    tar = tarfile.open(app_fname)
    tar.extractall(path=deploy_dir)
    tar.close()

    # 拼接出解压文件的绝对路径
    app_dir = os.path.basename(app_fname)
    app_dir = app_dir.replace('.tar.gz', '')
    app_dir = os.path.join(deploy_dir, app_dir)

    # 如果软链接已存在，先删除它
    if os.path.exists(dest):
        os.remove(dest)

    # 创建软链接
    os.symlink(app_dir, dest)

if __name__ == '__main__':
    # 判断是否有新版本
    ver_url = 'http://192.168.1.103/deploy/live_ver'
    ver_fname = '/var/www/deploy/live_ver'
    if not has_new_ver(ver_url, ver_fname):
        print('未发现新版本')
        exit(1)

    # 下载新版本软件
    download_dir = '/var/www/download'
    r = requests.get(ver_url)
    app_url = 'http://192.168.1.103/deploy/pkgs/myweb-%s.tar.gz' % r.text
    wget.download(app_url, download_dir)

    # 判断文件是否完好，如果损坏则删除它
    md5url = app_url + '.md5'
    app_fname = os.path.basename(app_url)
    app_fname = os.path.join(download_dir, app_fname)
    if not file_ok(md5url, app_fname):
        os.remove(app_fname)
        exit(2)

    # 部署软件
    deploy_dir = '/var/www/deploy'
    dest = '/var/www/html/nsd2002'
    deploy(app_fname, deploy_dir, dest)

    # 更新live_ver文件
    if os.path.exists(ver_fname):
        os.remove(ver_fname)
    wget.download(ver_url, ver_fname)
