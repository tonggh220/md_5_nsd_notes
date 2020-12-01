from django.shortcuts import render

# 用户发起的请求，请求将被封装成一个请求对象，作为第一个参数传给函数
# 因此，函数至少需要有一个参数接收
def index(request):
    # render是一个函数，它可以找到相关的网页模板，返回给用户
    return render(request, 'index.html')
