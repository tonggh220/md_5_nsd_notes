
def has_new_ver(ver_url, ver_fname):
    "用于判断是否有新版本，有返回True，否则返回False"


if __name__ == '__main__':
    # 检查是否有新版本
    ver_url = 'http://192.168.1.103/deploy/live_ver'
    ver_fname = '/var/www/deploy/live_ver'
    if not has_new_ver(ver_url, ver_fname):
        print("未发现新版本")
        exit(1)

    # 下载最新版本的代码

    # 如果下载的代码已损坏，则删除它

    # 部署代码

    # 更新本地版本
