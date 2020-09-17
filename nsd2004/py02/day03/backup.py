import os
import tarfile
from time import strftime


def full_backup(src, dst, md5file):
    "用于完全备份"
    # 拼接出备份文件的绝对路径
    fname = '%s_full_%s.tar.gz' % (os.path.basename(src), strftime('%Y%m%d'))
    fname = os.path.join(dst, fname)

    # 完全备份，就是把源目录直接打个压缩包
    tar = tarfile.open(fname, 'w:gz')
    tar.add(src)
    tar.close()

def incr_backup(src, dst, md5file):
    "用于增量备份"

if __name__ == '__main__':
    src = '/tmp/demo/security'
    dst = '/tmp/demo/backup'
    md5file = '/tmp/demo/backup/md5.data'
    if strftime('%a') == 'Mon':
        full_backup(src, dst, md5file)
    else:
        incr_backup(src, dst, md5file)

# mkdir -p /tmp/demo/backup
# cp -r /etc/security /tmp/demo
