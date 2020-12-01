from django.urls import path, re_path
from polls import views

urlpatterns = [
    # 从http://server/polls/后面开始匹配
    # 如果polls/后面为空，则调用views.py文件中的index函数
    # name='index'是给http://server/polls/这个url起的名字
    path('', views.index, name='index'),
    # path函数中的路径，支持变量。声明一个名为qid的变量，类型是int, 变量将会传递给detail函数
    # 变量类型还有str和slug，slug很少应用到
    path('<int:qid>', views.detail, name='detail'),
    # path函数也可以替换为正则表达式，如上面的写法，也可以写为：
    # re_path('^(\d+)$', views.detail, name='detail'),
    path('<int:qid>/result', views.result, name='result'),
]
