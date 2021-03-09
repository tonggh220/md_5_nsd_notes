from django.urls import path
from webadmin import views

urlpatterns = [
    path('', views.index, name='webadmin_index'),
]

