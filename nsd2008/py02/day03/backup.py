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
    md5dict = {}
    for path, folders, files in os.walk(src):
        for file in files:
            key = os.path.join(path, file)
            md5dict[key] = check_md5(key)

    # 把md5值存入文件
    with open(md5file, 'wb') as fobj:
        pickle.dump(md5dict, fobj)

def incr_backup(src, dst, md5file):
    "用于增量备份"
    # 拼接出备份文件名
    fname = "%s_incr_%s.tar.gz" % \
            (os.path.basename(src), strftime("%Y%m%d"))
    fname = os.path.join(dst, fname)

    # 计算每个文件的md5值
    md5dict = {}
    for path, folders, files in os.walk(src):
        for file in files:
            key = os.path.join(path, file)
            md5dict[key] = check_md5(key)

    # 取出前一天的md5值
    with open(md5file, 'rb') as fobj:
        old_md5 = pickle.load(fobj)

    # 找到新增的文件和变化的文件，进行备份
    tar = tarfile.open(fname, 'w:gz')
    for key in md5dict:
        # if key not in old_md5 or md5dict[key] != old_md5[key]:
        if old_md5.get(key) != md5dict[key]:
            tar.add(key)
    tar.close()

    # 更新md5file内容
    with open(md5file, 'wb') as fobj:
        pickle.dump(md5dict, fobj)

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
