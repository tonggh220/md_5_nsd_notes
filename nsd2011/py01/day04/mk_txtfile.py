import os

def get_fname():
    "用于获取一个系统中不存在的文件名"
    while 1:
        fname = input('文件名: ')
        # os.path.exists(fname)相当于shell的-e判断是否存在文件
        if not os.path.exists(fname):
            break
        print('文件已存在，请重试。')

    return fname

def get_content():
    "用于获取用户输入的多行文本"
    # 定义用于保存结果的列表
    content = []

    print('请输入内容，在单独的一行上输入end结束！')
    while 1:
        line = input('输入end结束> ')
        if line == 'end':
            break
        content.append(line)

    return content

def wfile(fname, content):
    "用于将内容content写入文件fname"

if __name__ == '__main__':
    # 获取文件名
    fname = get_fname()
    # 获取内容
    content = get_content()
    # 将内容写入文件
    wfile(fname, content)