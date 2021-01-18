from time import strftime
import os
import tarfile

def full_backup(src, dst, md5file):
    "用于完全备份"
    # 拼接出备份文件名
    fname = "%s_full_%s.tar.gz" % \
            (os.path.basename(src), strftime("%Y%m%d"))
    fname = os.path.join(dst, fname)

    # 打tar包
    tar = tarfile.open(fname, 'w:gz')
    tar.add(src)
    tar.close()

    # 计算每个文件的md5值

    # 把md5值存入文件

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
