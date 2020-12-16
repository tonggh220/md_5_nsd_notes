# mkdir -p /tmp/demo/backup
# cp -r /etc/security/ /tmp/demo/
from time import strftime
import os


def full_backup(src, dst, md5file):
    "完全备份"

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

