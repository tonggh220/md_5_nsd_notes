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
    '完全备份'
    # 拼接出备份文件的文件名
    fname = f'{os.path.basename(src)}_full_{strftime("%Y%m%d")}.tar.gz'
    fname = os.path.join(dst, fname)

    # 备份，打tar包
    with tarfile.open(fname, 'w:gz') as tar:
        tar.add(src)

    # 计算当前文件的md5值
    md5dict = {}



def incr_backup(src, dst, md5file):
    '增量备份'

if __name__ == '__main__':
    src = '/tmp/demo/security'
    dst = '/tmp/demo/backup'
    md5file = '/tmp/demo/backup/md5.data'
    # 如果是周一，或者从来没有备份过，则进行完全备份
    if (strftime('%a') == 'Mon') or (not os.path.exists(md5file)):
        full_backup(src, dst, md5file)
    else:
        incr_backup(src, dst, md5file)

# mkdir -p /tmp/demo/backup
# cp -r /etc/security /tmp/demo/
