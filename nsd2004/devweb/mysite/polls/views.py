from django.shortcuts import render
from polls.models import Question

# 用户发起的请求，请求将会成为一个对象，作为第一个参数传给函数
# 因此，函数至少需要有一个参数
def index(request):
    # 取出所有的问题，并按时间进行降序排列
    questions = Question.objects.order_by('-pub_date')
    # index函数通过render函数找到一个网页模板文件，返回给客户端
    return render(request, 'index.html', {'questions': questions})

def detail(request, qid):
    # qid用于接收来自于url的参数
    question = Question.objects.get(id=qid)
    # {'qid': qid}将成为detail.html的变量和值，即 qid=数字
    return render(request, 'detail.html', {'question': question})

def result(request, qid):
    return render(request, 'result.html', {'qid': qid})
