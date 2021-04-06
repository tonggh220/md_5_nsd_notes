from django.urls import path
from polls import views


urlpatterns = [
    # 从http://server_ip/polls/后面进行匹配
    # polls/后面空的，则调用相关函数views.index
    # name='index'是给http://server_ip/polls/起的名字
    path('', views.index, name='index'),
]
