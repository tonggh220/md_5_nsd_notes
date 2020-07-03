import wget
import requests
import os
import hashlib
import tarfile

def has_new_ver(ver_url, ver_fname):
    "用于检查是否有新版本，有则返回True，否则返回False"
    # 如果本地没有版本文件，则有新版本
    if not os.path.exists(ver_fname):
        return True

    # 如果本地和远程版本文件不一样，则有新版本
    with open(ver_fname) as fobj:
        local_ver = fobj.read()
    r = requests.get(ver_url)
    if local_ver != r.text:
        return True

    # 如果上述条件都不满足，则没有新版本
    return False


def check_file(md5url, fname):
    "用于检查文件是否损坏，未损坏返回True，否则返回False"
    # 计算本地文件的md5值
    m = hashlib.md5()
    with open(fname, 'rb') as fobj:
        while 1:
            data = fobj.read(4096)
            if not data:
                break
            m.update(data)

    # 取出网上md5值，进行比较
    r = requests.get(md5url)
    if m.hexdigest() == r.text.strip():  # 去除网上md5文件尾部\n
        return True

    # 如果本地和远程的md5值不一样，返回False
    return False

def deploy(app_fname, deploy_dir, dest):
    "用于部署程序到应用服务器"
    # 解压文件到目标
    tar = tarfile.open(app_fname)
    tar.extractall(path=deploy_dir)
    tar.close()

    # 拼接出解压目录的绝对路径
    app_dir = os.path.basename(app_fname)
    app_dir = app_dir.replace('.tar.gz', '')
    app_dir = os.path.join(deploy_dir, app_dir)

    # 创建快捷方式，如果快捷方式已存在，先删除它
    if os.path.exists(dest):
        os.remove(dest)

    os.symlink(app_dir, dest)

if __name__ == '__main__':
    # 检查是否有新版本，没有新版本退出
    ver_url = 'http://192.168.81.135/deploy/live_ver'
    ver_fname = '/var/www/deploy/live_ver'
    if not has_new_ver(ver_url, ver_fname):
        print('未发现新版本。')
        exit(1)

    # 下载新版本
    r = requests.get(ver_url)
    pkg_url = 'http://192.168.81.135/deploy/pkgs/myweb-%s.tar.gz' % r.text
    app_fname = '/var/www/download/myweb-%s.tar.gz' % r.text
    wget.download(pkg_url, app_fname)

    # 检查新版本程序文件是否损坏，如损坏则删除它并退出
    md5url = pkg_url + '.md5'
    if not check_file(md5url, app_fname):
        print('文件已损坏。')
        os.remove(app_fname)
        exit(2)

    # 部署软件
    deploy_dir = '/var/www/deploy'
    dest = '/var/www/html/nsd1912'
    deploy(app_fname, deploy_dir, dest)

    # 更新本地版本live_ver文件
    if os.path.exists(ver_fname):
        os.remove(ver_fname)
    wget.download(ver_url, ver_fname)
