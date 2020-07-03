from django.conf.urls import url
from polls import views

urlpatterns = [
    # 从http://x.x.x.x/polls/后面开始匹配
    # 如果用户访问http://x.x.x.x/polls/，则调用views.index函数
    # 将http://x.x.x.x/polls/这个url起名为index
    url(r'^$', views.index, name='index'),
    # \d+匹配问题id，加上()后，它将作为detail的参数
    url(r'^(\d+)/$', views.detail, name='detail'),
    url(r'^(\d+)/result/$', views.result, name='result'),
    url(r'^(\d+)/vote/$', views.vote, name='vote'),
]
