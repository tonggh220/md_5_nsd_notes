from django.urls import path
from polls import views

urlpatterns = [
    # 从http://127.0.0.1/polls/后面开始匹配
    # 如果polls/后面为空，则调用函数views.index进行处理
    # name='index'是给url http://127.0.0.1/polls/起的名字
    path('', views.index, name="index"),
]
