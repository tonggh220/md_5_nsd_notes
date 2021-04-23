from time import strftime
import os

def full_backup(src, dst, md5file):
    '完全备份'

def incr_backup(src, dst, md5file):
    '增量备份'

if __name__ == '__main__':
    src = '/tmp/demo/security'
    dst = '/tmp/demo/backup'
    md5file = '/tmp/demo/backup/md5.data'
    if (strftime('%a') == 'Mon') or (not os.path.exists(md5file)):
        full_backup(src, dst, md5file)
    else:
        incr_backup(src, dst, md5file)

# mkdir -p /tmp/demo/backup
# cp -r /etc/security /tmp/demo

