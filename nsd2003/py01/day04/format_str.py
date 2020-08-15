import mkfile

def format(content):
    width = 48  # 定义字符串宽度
    print('+%s+' % ('*' * width))  # +*****************+
    for line in content:  # 在字符串列表中，取出每个字符串
        # width - len(line)  得到字符串两边空格的总数
        m, n = divmod((width - len(line)), 2)
        # m是左边空格数目，m+n是右边空格数目
        print('+%s%s%s+' % (' ' * m, line, ' ' * (m + n)))
    print('+%s+' % ('*' * width))  # +*****************+

if __name__ == '__main__':
    content = mkfile.get_content()
    format(content)
