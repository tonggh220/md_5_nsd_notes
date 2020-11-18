import os
import tarfile
import hashlib
from time import strftime

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
    "完全备份"
    # 拼接出备份文件名
    fname = "%s_full_%s.tar.gz" % (os.path.basename(src), strftime("%Y%m%d"))
    fname = os.path.join(dst, fname)

    # 打tar包
    tar = tarfile.open(fname, 'w:gz')
    tar.add(dst)
    tar.close()

    # 计算每个文件的md5值
    md5dict = {}
    

    # 将md5字典保存到文件

def incr_backup(src, dst, md5file):
    "增量备份"
    print('incr backup')

if __name__ == '__main__':
    src = '/tmp/demo/security'
    dst = '/tmp/demo/backup'
    md5file = '/tmp/demo/backup/md5.data'
    if strftime('%a') == 'Mon' or not os.path.exists(md5file):
        full_backup(src, dst, md5file)
    else:
        incr_backup(src, dst, md5file)

# mkdir -p /tmp/demo/backup
# cp -r /etc/security/ /tmp/demo/
