from django.shortcuts import render

# 用户发起的请求，请求将会成为一个对象，作为第一个参数传给函数
# 因此，函数至少需要有一个参数
def index(request):
    # index函数通过render函数找到一个网页模板文件，返回给客户端
    return render(request, 'index.html')

# qid用于接收来自于url的参数
def detail(request, qid):
    # {'qid': qid}将成为detail.html的变量和值，即 qid=数字
    return render(request, 'detail.html', {'qid': qid})

def result(request, qid):
    # {'qid': qid}将成为detail.html的变量和值，即 qid=数字
    return render(request, 'result.html', {'qid': qid})

