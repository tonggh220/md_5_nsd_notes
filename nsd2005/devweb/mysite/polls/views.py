from django.shortcuts import render, redirect
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
    question = Question.objects.get(id=qid)
    return render(request, 'result.html', {'question': question})

def vote(request, qid):
    # print('-' * 30)
    # print(dir(request))
    # print('-' * 30)
    # print(request.POST)
    question = Question.objects.get(id=qid)
    # request有名为POST的属性，存储用户通过Post方法提交的数据。它是一个字典对象
    choice_id = request.POST.get('choice_id')
    # 取出相应的选项，并把票数加1
    choice = question.choice_set.get(id=choice_id)
    choice.votes += 1
    choice.save()
    # 重定向到投票结果页, result是urls.py中定义的url名称
    return redirect('result', qid)
