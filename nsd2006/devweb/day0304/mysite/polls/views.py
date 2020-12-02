from django.shortcuts import render
from polls.models import Question

# 用户发起的请求，请求将被封装成一个请求对象，作为第一个参数传给函数
# 因此，函数至少需要有一个参数接收
def index(request):
    # 取出所有问题，按时间降序排列
    questions = Question.objects.order_by('-pub_date')
    # render是一个函数，它可以找到相关的网页模板，返回给用户
    return render(request, 'index.html', {'questions': questions})

def detail(request, qid):
    # qid用于接收来自于url的参数
    # {'qid': qid}将成为detail.html中的变量和值，即 qid=数字
    return render(request, 'detail.html', {'qid': qid})

def result(request, qid):
    return render(request, 'result.html', {'qid': qid})
