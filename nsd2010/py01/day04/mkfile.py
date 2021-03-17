def get_fname():
    "用于获取一个系统中不存在的文件名"

def get_content():
    "用于获取用户输入的多行文本"

def wfile(fname, content):
    "用于将内容content写入文件fname"

if __name__ == '__main__':
    # 获取文件名
    fname = get_fname()
    # 获取内容
    content = get_content()
    # 将内容写入文件
    wfile(fname, content)