from django.urls import path
from polls import views

urlpatterns = [
    # 从http://x.x.x.x/polls/后面开始匹配
    # 如果poll/后面为空，则调用views.py中index函数
    # name='index'是给http://x.x.x.x./polls/这个url起的名
    path('', views.index, name='index'),
]
