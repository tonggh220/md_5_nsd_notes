import os
import tarfile
import hashlib
import pickle
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
    fname = '%s_full_%s.tar.gz' % (os.path.basename(src), strftime('%Y%m%d'))
    fname = os.path.join(dst, fname)

    # 备份，即打tar包
    tar = tarfile.open(fname, 'w:gz')
    tar.add(src)
    tar.close()

    # 计算文件md5值
    md5dict = {}
    for path, folders, files in os.walk(src):
        for file in files:
            k = os.path.join(path, file)
            md5dict[k] = check_md5(k)

    # 保存md5值到文件
    with open(md5file, 'wb') as fobj:
        pickle.dump(md5dict, fobj)

def incr_backup(src, dst, md5file):
    "增量备份"
    # 拼接出备份文件名
    fname = '%s_incr_%s.tar.gz' % (os.path.basename(src), strftime('%Y%m%d'))
    fname = os.path.join(dst, fname)

    # 计算文件md5值
    md5dict = {}
    for path, folders, files in os.walk(src):
        for file in files:
            k = os.path.join(path, file)
            md5dict[k] = check_md5(k)

    # 取出前一天的md5值
    with open(md5file, 'rb') as fobj:
        old_md5 = pickle.load(fobj)

    # 找到改变的文件和新增的文件，进行备份
    tar = tarfile.open(fname, 'w:gz')
    for k in md5dict:
        # if (k not in old_md5) or (md5dict[k] != old_md5[k]):
        if old_md5.get(k) != md5dict[k]:
            tar.add(k)
    tar.close()

    # 保存新md5值到文件
    with open(md5file, 'wb') as fobj:
        pickle.dump(md5dict, fobj)

if __name__ == '__main__':
    src = '/tmp/demo/security'
    dst = '/tmp/demo/backup'
    md5file = '/tmp/demo/backup/md5.data'
    if (strftime('%a') == 'Mon') or (not os.path.exists(md5file)):
        full_backup(src, dst, md5file)
    else:
        incr_backup(src, dst, md5file)

# mkdir -p /tmp/demo/backup
# cp -r /etc/security/ /tmp/demo


