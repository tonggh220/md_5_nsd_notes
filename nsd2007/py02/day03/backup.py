# mkdir -p /tmp/demo/backup
# cp -r /etc/security/ /tmp/demo/
from time import strftime
import os
import tarfile
import hashlib
import pickle

def check_md5(fname):
    "接收文件名，返回md5值"
    m = hashlib.md5()
    with open(fname, 'rb') as fobj:
        while 1:
            data = fobj.read(4096)
            if not data:
                break
            m.update(data)

    return m.hexdigest()


def full_backup(src, dst, md5file):
    "完全备份"
    # 拼接备份目标文件的绝对路径
    fname = '%s_full_%s.tar.gz' % (os.path.basename(src), strftime('%Y%m%d'))
    fname = os.path.join(dst, fname)

    # 实现完全备份，也就是把整个目录打tar包
    tar = tarfile.open(fname, 'w:gz')
    tar.add(src)
    tar.close()

    # 计算每个文件的md5值
    md5dict = {}
    for path, folders, files in os.walk(src):
        for file in files:
            key = os.path.join(path, file)
            md5dict[key] = check_md5(key)

    # 将md5字典与入文件
    with open(md5file, 'wb') as fobj:
        pickle.dump(md5dict, fobj)

def incr_backup(src, dst, md5file):
    "增量备份"

if __name__ == '__main__':
    src = '/tmp/demo/security'
    dst = '/tmp/demo/backup'
    md5file = '/tmp/demo/backup/md5.data'
    # 如果是周一，或者md5文件不存在都要执行完全备份
    if strftime('%a') == 'Mon' or not os.path.isfile(md5file):
        full_backup(src, dst, md5file)
    else:
        incr_backup(src, dst, md5file)

