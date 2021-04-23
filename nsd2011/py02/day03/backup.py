from time import strftime
import os
import tarfile
import hashlib

def check_md5(fname):
    m = hashlib.md5()

    with open(fname, 'rb') as fobj:
        while 1:
            data = fobj.read(4096)
            if not data:
                break
            m.update(data)

    return m.hexdigest()

def full_backup(src, dst, md5file):
    '完全备份'
    # 拼接备份文件的文件名
    fname = f'{os.path.basename(src)}_full_{strftime("%Y%m%d")}.tar.gz'
    fname = os.path.join(dst, fname)

    # 完全备份，打tar包
    with tarfile.open(fname, 'w:gz') as tar:
        tar.add(src)

def incr_backup(src, dst, md5file):
    '增量备份'

if __name__ == '__main__':
    src = '/tmp/demo/security'  # 源
    dst = '/tmp/demo/backup'    # 目标目录
    md5file = '/tmp/demo/backup/md5.data'  # md5文件
    # 如果是周一或从来没有备份过，就进行完全备份
    if (strftime('%a') == 'Mon') or (not os.path.exists(md5file)):
        full_backup(src, dst, md5file)
    else:
        incr_backup(src, dst, md5file)

# mkdir -p /tmp/demo/backup
# cp -r /etc/security /tmp/demo

