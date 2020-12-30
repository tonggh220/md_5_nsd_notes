from django.shortcuts import render
from polls.models import Question

# 用户发起的请求，将会成为一个请求对象，作为第一个参数传给函数
# 因此，函数至少需要有一个参数进行接收
def index(request):
    # 取出所有的问题，按发布时间降序排列
    questions = Question.objects.order_by('-pub_date')
    # 通过render函数找到一个网页模板文件，返回给客户端
    return render(request, 'index.html', {'questions': questions})

def detail(request, qid):
    # qid用于接收来自于url的参数qid
    # 取出指定的问题，将其发给前端网页
    question = Question.objects.get(id=qid)
    return render(request, 'detail.html', {'question': question})
    # {'qid': qid}将成为detail.html中的变量和值，即 qid=数字
    # return render(request, 'detail.html', {'qid': qid})

def result(request, qid):
    return render(request, 'result.html', {'qid': qid})

def vote(request, qid):
    print('-' * 50)
    print(dir(request))
    print('-' * 50)
    print(request.POST)
    print('-' * 50)
    return render(request, 'result.html')
