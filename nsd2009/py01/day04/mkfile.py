import os

def get_fname():
    "用于获取一个系统中不存在的文件名"
    while 1:
        fname = input("文件名: ")
        if not os.path.exists(fname):
            break
        print("文件已存在，请重试。")

    return fname

def get_content():
    "用于获取用户输入的多行文本"
    content = []

    print("请输入内容，在单独的一行上输入end结束！")
    while 1:
        line = input("(输入end结束)> ")
        if line == "end":
            break
        content.append(line)
        # content.append(line + '\n')

    return content

def wfile(fname, content):
    "用于将内容content写入文件fname"
    with open(fname, 'w') as fobj:
        fobj.writelines(content)

if __name__ == '__main__':
    # 获取文件名
    fname = get_fname()
    # 获取内容
    content = get_content()
    # 将列表中每个字符串结尾增加\n
    content = ['%s\n' % line for line in content]
    # 将内容写入文件
    wfile(fname, content)
