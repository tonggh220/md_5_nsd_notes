import requests
import wget
import os

def has_new_ver(ver_url, ver_fname):
    "判断是否有新版本，有返回True，否则为False"


def file_ok(md5url, app_fname):
    "校验文件是否完好，完好返回True，否则为False"

if __name__ == '__main__':
    # 判断是否有新版本
    ver_url = 'http://192.168.1.103/deploy/live_ver'
    ver_fname = '/var/www/deploy/live_ver'
    if not has_new_ver(ver_url, ver_fname):
        print("未发现新版本。")
        exit(1)

    # 下载新版本软件包
    download_dir = '/var/www/download'
    r = requests.get(ver_url)
    app_url = 'http://192.168.1.103/deploy/pkgs/myweb-%s.tar.gz' % r.text
    wget.download(app_url, download_dir)

    # 检查软件包是否损坏，如已损坏则删除它
    md5url = app_url + '.md5'
    app_fname = app_url.split('/')[-1]
    app_fname = os.path.join(download_dir, app_fname)
    if not file_ok(md5url, app_fname):
        print("文件已损坏")
        os.remove(app_fname)
        exit(2)

    # 部署软件

    # 更新本地版本文件
