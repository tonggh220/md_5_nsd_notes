import requests
import wget

def has_new_ver(ver_url, ver_fname):
    "用于判断是否有新版本，有返回True，没有返回False"



if __name__ == '__main__':
    # 判断是否有新版本，没有新版本则退出
    ver_url = 'http://192.168.1.103/deploy/live_ver'
    ver_fname = '/var/www/html/deploy/live_ver'
    if not has_new_ver(ver_url, ver_fname):
        print("未发现新版本")
        exit(1)

    # 下载新版本软件
    download_dir = "/var/www/download"
    r = requests.get(ver_url)
    app_url = "http://192.168.1.103/deploy/pkgs/myweb-%s.tar.gz" % r.text
    wget.download(app_url, download_dir)

    # 校验新版本文件，如果已损坏则删除

    # 部署软件

    # 更新本地live_ver文件
