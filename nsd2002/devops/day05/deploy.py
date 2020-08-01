import os
import requests


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


def file_ok():
    "判断文件是否完好，完好返回True，否则为False"


def deploy():
    "部署软件"

if __name__ == '__main__':
    # 判断是否有新版本
    ver_url = 'http://192.168.1.103/deploy/live_ver'
    ver_fname = '/var/www/deploy/live_ver'
    if not has_new_ver(ver_url, ver_fname):
        print('未发现新版本')
        exit(1)

    # 下载新版本软件

    # 判断文件是否完好，如果损坏则删除它
    if not file_ok():
        os.remove()
        exit(2)

    # 部署软件

    # 更新live_ver文件
