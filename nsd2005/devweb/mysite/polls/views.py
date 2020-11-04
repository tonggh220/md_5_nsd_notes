from django.shortcuts import render
from polls.models import Question

# 用户发起的请求，请求对象将会自动成为第一个参数传给函数
def index(request):
    questions = Question.objects.order_by('-pub_date')
    # 通过render函数找到名为index.html的网页模板，返回给客户端
    return render(request, 'index.html', {'questions': questions})

def detail(request, qid):
    # qid用于接受来自于url的变量
    question = Question.objects.get(id=qid)
    return render(request, 'detail.html', {'question': question})
    # {'qid': qid}将成为detial.html的变量和值，即qid=数字
    # return render(request, 'detail.html', {'qid': qid})

def result(request, qid):
    return render(request, 'result.html', {'qid': qid})
