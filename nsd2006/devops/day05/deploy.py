import requests
import wget
import os


def has_new_ver(ver_url, ver_fname):
    "用于检查是否有新版本，有返回True，否则返回False"

def file_ok(md5url, app_fname):
    "判断文件是否完好。完好返回True，否则返回False"

if __name__ == '__main__':
    # 判断是否有新版本，没有新版本就退出
    ver_url = 'http://192.168.1.103/deploy/live_ver'
    ver_fname = '/var/www/deploy/live_ver'
    if not has_new_ver(ver_url, ver_fname):
        print("未发现新版本")
        exit(1)

    # 下载新版本软件
    download_dir = '/var/www/download'
    r = requests.get(ver_url)
    app_url = 'http://192.168.1.103/deploy/pkgs/myweb-%s.tar.gz' % r.text
    wget.download(app_url, download_dir)

    # 判断下载的文件是否完整，如果已损坏则删除它
    md5url = app_url + '.md5'
    app_fname = app_url.split('/')[-1]
    app_fname = os.path.join(download_dir, app_fname)
    if not file_ok(md5url, app_fname):
        os.remove(app_fname)
        exit(2)

    # 部署软件

    # 更新本地的版本文件live_ver
