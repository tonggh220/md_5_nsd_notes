from time import strftime
import os
import tarfile
import hashlib
import pickle

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

    # 计算文件md5值
    md5dict = {}
    for path, folders, files in os.walk(src):
        for file in files:
            key = os.path.join(path, file)
            md5dict[key] = check_md5(key)

    # 保存md5字典到md5file
    with open(md5file, 'wb') as fobj:
        pickle.dump(md5dict, fobj)

def incr_backup(src, dst, md5file):
    '增量备份'
    # 拼接备份文件的文件名
    fname = f'{os.path.basename(src)}_incr_{strftime("%Y%m%d")}.tar.gz'
    fname = os.path.join(dst, fname)

    # 计算文件md5值
    md5dict = {}
    for path, folders, files in os.walk(src):
        for file in files:
            key = os.path.join(path, file)
            md5dict[key] = check_md5(key)

    # 取出前一天的md5值
    with open(md5file, 'rb') as fobj:
        old_md5 = pickle.load(fobj)

    # 找到新增文件和改变的文件，进行备份

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

