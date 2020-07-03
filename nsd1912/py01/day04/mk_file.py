import os


def get_fname():
    "用于获取一个不存在的文件名"
    while 1:
        fname = input('文件名: ')
        if not os.path.exists(fname):  # 如果文件不存在
            break
        print('文件已存在，请重试。')

    return fname


def get_content():
    "用于获取内容"
    content = []  # 定义用于保存内容的列表

    print('请输入内容，单独一行输入end结束。')
    while 1:
        line = input('(end to quit)> ')
        if line == 'end':
            break
        content.append(line)

    return content


def wfile(fname, content):
    "用于将内容content写入到文件fname中"
    with open(fname, 'w') as fobj:
        fobj.writelines(content)


if __name__ == '__main__':
    fname = get_fname()
    content = get_content()
    content = ['%s\n' % line for line in content]
    wfile(fname, content)
