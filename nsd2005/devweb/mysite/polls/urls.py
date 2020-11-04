from django.urls import path, re_path
from polls import views

urlpatterns = [
    # 从http://server_ip/polls/后面进行匹配
    # 访问http://server_ip/polls/时，调用views.index函数
    # 给http://server_ip/polls/这个网址起名为index
    path('', views.index, name='index'),
    # path函数接受变量，声明一个名为qid的变量，类型是int
    # 类型除int外，还有str和slug
    path('<int:qid>', views.detail, name='detail'),
    path('<int:qid>/result', views.result, name='result'),
    # re_path表示使用正则表达式，括号用于保存数据并作为参数传给函数
    # re_path(r'^(\d+)$', views.detail, name='detail')
    path('<int:qid>/vote', views.vote, name='vote'),
]
