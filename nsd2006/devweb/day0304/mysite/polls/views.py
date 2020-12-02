from django.shortcuts import render, redirect
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
    question = Question.objects.get(id=qid)
    return render(request, 'detail.html', {'question': question})
    # {'qid': qid}将成为detail.html中的变量和值，即 qid=数字
    # return render(request, 'detail.html', {'qid': qid})

def result(request, qid):
    question = Question.objects.get(id=qid)
    return render(request, 'result.html', {'question': question})

def vote(request, qid):
    question = Question.objects.get(id=qid)
    # request有一个名为POST的属性，存储用户通过post方法提供的数据。它是一个类字典对象
    choice_id = request.POST.get('choice_id')
    # print('-' * 50)
    # print(dir(request))
    # print('-' * 50)
    # print(request.POST)
    # print('-' * 50)
    # 取出选项实例，将其票数加1
    choice = question.choice_set.get(id=choice_id)
    choice.votes += 1
    choice.save()
    # 投票完成后，转向到结果页
    return redirect('result', qid)
