from django.shortcuts import render, redirect
from polls.models import Question

# 用户发起的请求，将会被django作为第一个参数传给函数，所以函数需要有一个参数
def index(request):
    questions = Question.objects.order_by('-pub_date')
    # 通过render函数找到名为index.hml的网页模板文件，返回给用户
    return render(request, 'index.html', {'questions': questions})

def detail(request, qid):
    # qid用于接收从url传来的参数
    question = Question.objects.get(id=qid)
    # 字典中的内容将以关键字参数key=val的形式传给网页模板，如qid=10
    return render(request, 'detail.html', {'question': question})

def result(request, qid):
    question = Question.objects.get(id=qid)
    return render(request, 'result.html', {'question': question})

def vote(request, qid):
    # 取出待投票的问题
    question = Question.objects.get(id=qid)
    # 取出前端网页发送过来的选项id
    # request保存的是用户请求，它是一个像字典一样的结构，可以通过request.POST得到post数据
    # request.post也是一个字典结构，可以通过key取出val
    cid = request.POST.get('cid')
    # 取出choice_id对应的选项实例
    choice = question.choice_set.get(id=cid)
    choice.votes += 1  # 票数加1
    choice.save()
    # 投票完成后，跳转到投票结果页，result的结果url的名字
    return redirect('result', qid)
