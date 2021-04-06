from django.urls import path
from polls import views


urlpatterns = [
    # 从http://server_ip/polls/后面进行匹配
    # polls/后面空的，则调用相关函数views.index
    # name='index'是给http://server_ip/polls/起的名字
    path('', views.index, name='index'),
    # path()函数中的路径，可以支持变量。声明一个名为qid，类型为int的变量
    # 类型除了int外，还有str和slug
    path('<int:qid>', views.detail, name='detail'),
]
