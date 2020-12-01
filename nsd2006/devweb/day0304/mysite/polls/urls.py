from django.urls import path
from polls import views

urlpatterns = [
    # 从http://server/polls/后面开始匹配
    # 如果polls/后面为空，则调用views.py文件中的index函数
    # name='index'是给http://server/polls/这个url起的名字
    path('', views.index, name='index'),
]
