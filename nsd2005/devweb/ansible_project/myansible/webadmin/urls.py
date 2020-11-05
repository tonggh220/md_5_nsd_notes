from django.urls import path
from webadmin import views

urlpatterns = [
    path('', views.index, name='webadmin_index'),
    path('add_hosts', views.add_hosts, name='add_hosts'),
]
