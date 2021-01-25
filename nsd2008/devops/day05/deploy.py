import requests
import wget
import os

def has_new_ver(ver_url, ver_fname):
    "用于判断是否有新版本，有返回True，否则返回False"

def file_ok(md5url, app_fname):
    "如果md5值一样返回True，否则返回False"

def deploy(app_fname, deploy_dir, dest):
    "部署软件"

if __name__ == '__main__':
    # 检查是否有新版本
    ver_url = 'http://192.168.1.103/deploy/live_ver'
    ver_fname = '/var/www/deploy/live_ver'
    if not has_new_ver(ver_url, ver_fname):
        print("未发现新版本")
        exit(1)

    # 下载最新版本的代码
    download_dir = '/var/www/download'
    r = requests.get(ver_url)
    app_url = 'http://192.168.1.103/deploy/pkgs/myweb-%s.tar.gz' % r.text
    wget.download(app_url, download_dir)

    # 如果下载的代码已损坏，则删除它
    md5url = app_url + '.md5'
    app_fname = app_url.split('/')[-1]
    app_fname = os.path.join(download_dir, app_fname)
    if not file_ok(md5url, app_fname):
        os.remove(app_fname)
        print("文件已损坏，请重新下载")
        exit(2)

    # 部署代码
    deploy_dir = '/var/www/deploy'
    dest = '/var/www/html/nsd2008'
    deploy(app_fname, deploy_dir, dest)

    # 更新本地版本
    if os.path.exists(ver_fname):
        os.remove(ver_fname)
    wget.download(ver_url, ver_fname)
