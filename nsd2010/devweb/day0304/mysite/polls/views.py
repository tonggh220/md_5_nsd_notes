from django.shortcuts import render, redirect
from polls.models import Question

# 用户发起的请求，请求将会成为一个对象，作为第一个参数传给函数
# 因此，函数至少需要有一个参数
def index(request):
    # 取出所有的问题，按时间降序排列
    questions = Question.objects.order_by('-pub_date')
    # index函数通过render函数找到一个网页模板文件，返回给客户端
    return render(request, 'index.html', {'questions': questions})

def detail(request, qid):   # qid用于接收来自于url的参数
    question = Question.objects.get(id=qid)
    return render(request, 'detail.html', {'question': question})

    # {'qid': qid}将成为detail.html的变量和值，即 qid=数字
    # return render(request, 'detail.html', {'qid': qid})

def result(request, qid):   # qid用于接收来自于url的参数
    # {'qid': qid}将成为detail.html的变量和值，即 qid=数字
    return render(request, 'result.html', {'qid': qid})

def vote(request, qid):
    question = Question.objects.get(id=qid)
    # 从request中取出用户的选项
    choice_id = request.POST.get('choice_id')
    # 取出相应的选项实例，并将票数加1
    choice = question.choice_set.get(id=choice_id)
    choice.votes += 1
    choice.save()
    # 投票结束后，跳转到结果页
    return redirect('result', question.id)

    # print('#' * 50)
    # print(dir(request))  # 查看request有哪些属性
    # print('#' * 50)
    # print(request.method)  # 查看request使用的方法
    # print('#' * 50)
    # print(request.POST)    # request.POST是一个类字典对象，记录表单数据
    # print('#' * 50)
    # return render(request, 'result.html')
