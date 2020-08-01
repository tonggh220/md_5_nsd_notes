import os


def has_new_ver():
    "判断是否有新版本，有返回True，否则为False"


def file_ok():
    "判断文件是否完好，完好返回True，否则为False"


def deploy():
    "部署软件"

if __name__ == '__main__':
    # 判断是否有新版本
    if not has_new_ver():
        print('未发现新版本')
        exit(1)

    # 下载新版本软件

    # 判断文件是否完好，如果损坏则删除它
    if not file_ok():
        os.remove()
        exit(2)

    # 部署软件

    # 更新live_ver文件
