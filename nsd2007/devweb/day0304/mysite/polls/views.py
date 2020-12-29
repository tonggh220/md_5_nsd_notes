from django.shortcuts import render

# 用户发起的请求，将会成为一个请求对象，作为第一个参数传给函数
# 因此，函数至少需要有一个参数进行接收
def index(request):
    # 通过render函数找到一个网页模板文件，返回给客户端
    return render(request, 'index.html')
