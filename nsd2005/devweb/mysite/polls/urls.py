from django.urls import path
from polls import views

urlpatterns = [
    # 从http://server_ip/polls/后面进行匹配
    # 访问http://server_ip/polls/时，调用views.index函数
    # 给http://server_ip/polls/这个网址起名为index
    path('', views.index, name='index'),
    # path函数接受变量，声明一个名为qid的变量，类型是int
    # 类型除int外，还有str和slug
    path('<int:qid>', views.detail, name='detail'),
]
