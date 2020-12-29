from django.urls import path
from polls import views

urlpatterns = [
    # 从http://x.x.x.x/polls/后面开始匹配
    # 如果poll/后面为空，则调用views.py中index函数
    # name='index'是给http://x.x.x.x./polls/这个url起的名
    path('', views.index, name='index'),
    # path()函数中的路径，可以支持变量。声明一个名为qid、类型为int的变量
    # qid指的是问题编号。除了int类型外，还可以有str和slug。slug基本不用
    path('<int:qid>', views.detail, name='detail'),
]
