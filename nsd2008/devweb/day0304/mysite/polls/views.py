from django.shortcuts import render
from polls.models import Question

# 用户发起请求，请求将为成为一个对象，作为第一个参数传给函数
# 因此，函数至少有一个参数，名字自定义
def index(request):
    # 取出所有的问题，按时间降序排列
    questions = Question.objects.order_by('-pub_date')
    # 通过render函数找到名为index.html的网页模板文件，返回给用户
    return render(request, 'index.html', {'questions': questions})

def detail(request, qid):
    # qid用于接收来自于url的参数
    question = Question.objects.get(id=qid)
    return render(request, 'detail.html', {'question': question})
    # {'qid': qid}将成为detail.html的变量和值，即：qid=数字
    # return render(request, 'detail.html', {'qid': qid})

def result(request, qid):
    return render(request, 'result.html', {'qid': qid})

def vote(request, qid):
    question = Question.objects.get(id=qid)
    
    return render(request, 'result.html', {'qid': qid})
