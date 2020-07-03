"""
备份程序

支持完全备份和增量备份。
mkdir -p /tmp/demo/backup
cp -r /etc/security /tmp/demo
"""
from time import strftime
import tarfile
import os
import hashlib
import pickle

def check_md5(fname):
    "用于计算并返回文件的md5值"
    m = hashlib.md5()
    with open(fname, 'rb') as fobj:
        while 1:
            data = fobj.read(4096)
            if not data:
                break
            m.update(data)

    return m.hexdigest()

def full_backup(src, dst, md5file):
    "实现完全备份"
    # 拼接出备份文件的绝对路径
    fname = '%s_full_%s.tar.gz' % (os.path.basename(src), strftime('%Y%m%d'))
    fname = os.path.join(dst, fname)

    # 将备份目录打tar包
    tar = tarfile.open(fname, 'w:gz')
    tar.add(src)
    tar.close()

    # 计算文件的md5值
    md5dict = {}
    for path, folders, files in os.walk(src):
        for file in files:
            k = os.path.join(path, file)
            md5dict[k] = check_md5(k)

    # 保存md5值到文件
    with open(md5file, 'wb') as fobj:
        pickle.dump(md5dict, fobj)

def incr_backup(src, dst, md5file):
    "实现增量备份"
    # 拼接出备份文件的绝对路径
    fname = '%s_incr_%s.tar.gz' % (os.path.basename(src), strftime('%Y%m%d'))
    fname = os.path.join(dst, fname)

    # 计算文件的md5值
    md5dict = {}
    for path, folders, files in os.walk(src):
        for file in files:
            k = os.path.join(path, file)
            md5dict[k] = check_md5(k)

    # 取出前一天的md5
    with open(md5file, 'rb') as fobj:
        old_md5 = pickle.load(fobj)

    # 找到新增文件和改动文件进行备份
    tar = tarfile.open(fname, 'w:gz')
    for key in md5dict:
        if old_md5.get(key) != md5dict[key]:
            tar.add(key)
    tar.close()

    # 更新md5file
    with open(md5file, 'wb') as fobj:
        pickle.dump(md5dict, fobj)

if __name__ == '__main__':
    src = '/tmp/demo/security'
    dst = '/tmp/demo/backup'
    md5file = '/tmp/demo/backup/md5.data'
    if strftime('%a') == 'Mon':
        full_backup(src, dst, md5file)
    else:
        incr_backup(src, dst, md5file)
