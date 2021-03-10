from django.urls import path
from webadmin import views

urlpatterns = [
    path('', views.index, name='webadmin_index'),
    path('add_hosts', views.add_hosts, name='add_hosts'),
    path('add_modules', views.add_modules, name='add_modules'),
    path('tasks', views.tasks, name='tasks'),
]

