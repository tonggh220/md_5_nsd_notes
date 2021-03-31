

def has_new_ver(ver_url, ver_fname):
    '如果有新版本返回True，否则返回False'


if __name__ == '__main__':
    # 判断是否有新版本，没有则退出
    ver_url = 'http://192.168.1.103/deploy/live_ver'
    ver_fname = '/var/www/deploy/live_ver'
    if not has_new_ver(ver_url, ver_fname):
        print('未发现新版本')
        exit(1)

    # 下载新版本软件包

    # 判断文件是否完好，如已损坏则删除它并退出

    # 部署软件

    # 更新本地版本
