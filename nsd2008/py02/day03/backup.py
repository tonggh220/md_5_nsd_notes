from time import strftime
import os

def full_backup(src, dst, md5file):
    "用于完全备份"

def incr_backup(src, dst, md5file):
    "用于增量备份"

if __name__ == '__main__':
    src = '/tmp/demo/security'
    dst = '/tmp/demo/backup'
    md5file = '/tmp/demo/backup/md5.data'
    # 如果是周一，或者是第一次备份，都执行完全备份
    if (strftime("%a") == "Mon") or (not os.path.exists(md5file)):
        full_backup(src, dst, md5file)
    else:
        incr_backup(src, dst, md5file)

# mkdir -p /tmp/demo/backup
# cp -r /etc/security /tmp/demo/
