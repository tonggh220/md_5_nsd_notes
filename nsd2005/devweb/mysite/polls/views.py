from django.shortcuts import render

# 用户发起的请求，请求对象将会自动成为第一个参数传给函数
def index(request):
    # 通过render函数找到名为index.html的网页模板，返回给客户端
    return render(request, 'index.html')
