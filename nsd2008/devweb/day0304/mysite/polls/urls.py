from django.urls import path, re_path
from polls import views

urlpatterns = [
    # 从http://127.0.0.1/polls/后面开始匹配
    # 如果polls/后面为空，则调用函数views.index进行处理
    # name='index'是给url http://127.0.0.1/polls/起的名字
    path('', views.index, name="index"),
    # path()函数中的路径，可以支持变。声明名为qid的变量，类型为int
    # 类型除int外，还可以用str和slug。slug不常用
    path('<int:qid>', views.detail, name='detail'),
    # path函数也可以使用正则表达式，如上面的写法可以替换为：
    # re_path(r'^(\d+)$', views.detail, name='detail')
    path('<int:qid>/result', views.result, name='result'),
    path('<int:qid>/vote', views.vote, name='vote'),
]
