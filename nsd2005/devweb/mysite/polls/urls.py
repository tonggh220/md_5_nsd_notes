from django.urls import path
from polls import views

urlpatterns = [
    # 从http://server_ip/polls/后面进行匹配
    # 访问http://server_ip/polls/时，调用views.index函数
    # 给http://server_ip/polls/这个网址起名为index
    path('', views.index, name='index'),
]
