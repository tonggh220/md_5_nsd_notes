import os
import wget
import requests


def has_new_ver(ver_url, ver_fname):
    "检查是否有新版本，有返回True，没有返回False"

def file_ok(md5url, app_fname):
    "检查文件是否完好，完好返回True，否则返回False"

def deploy(app_fname, deploy_dir, dest):
    "部署软件"

if __name__ == '__main__':
    # 检查是否有新版本，没有新版本就退出
    ver_url = 'http://192.168.1.103/deploy/live_ver'
    ver_fname = '/var/www/deploy/live_ver'
    if not has_new_ver(ver_url, ver_fname):
        print("未发现新版本。")
        exit(1)

    # 下载新版本软件
    download_dir = '/var/www/download'
    r = requests.get(ver_url)
    app_url = 'http://192.168.1.103/deploy/pkgs/myweb-%s.tar.gz' % r.text
    wget.download(app_url, download_dir)

    # 检查文件是否完好，如已损坏则删除并退出
    md5url = app_url + '.md5'
    app_fname = app_url.split('/')[-1]
    app_fname = os.path.join(download_dir, app_fname)
    if not file_ok(md5url, app_fname):
        print("文件已损坏。")
        os.remove(app_fname)
        exit(2)

    # 部署软件
    deploy_dir = '/var/www/deploy'
    dest = '/var/www/html/nsd2007'
    deploy(app_fname, deploy_dir, dest)

    # 更新版本号
    if os.path.exists(ver_fname):
        os.remove(ver_fname)
    wget.download(ver_url, ver_fname)
