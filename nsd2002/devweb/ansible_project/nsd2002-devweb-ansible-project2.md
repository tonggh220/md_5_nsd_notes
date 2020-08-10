# nsd2002-devweb-ansible-project2

## 实现添加主机功能

- 添加主机的url是http://127.0.0.1:9000/webadmin/add_hosts，该url也能展示web页面
  - 该url对应的函数就应该能接收两种请求，一种为get，一种为Post

```python
# 修改templates/webadmin/add_hosts.html，将表单的方法改为post
    <form action="{% url 'add_hosts' %}" class="form-inline h4" method="post">
        {% csrf_token %}
        ... ...
    </form>

# 修改视图函数，判断如果request.method是POST，则取出表单提交的数据。并在数据库中添加相应的条目
# 函数的request参数有一个名为method的属性，记录了http的方法是什么
# webadmin/views.py
def add_hosts(request):
    if request.method == 'POST':
        group = request.POST.get('group').strip()  # 去除字符串两边额外的空格
        host = request.POST.get('host').strip()
        ip = request.POST.get('ip').strip()
        if group:  # 如果group非空
            # 创建或取出组实例
            g = HostGroup.objects.get_or_create(groupname=group)[0]
            if host and ip:  # 如果host和ip也是非空的
                g.host_set.get_or_create(hostname=host, ip_addr=ip)

    # 在数据库中取出所有的组，发往前端
    groups = HostGroup.objects.all()
    return render(request, 'webadmin/add_hosts.html', {'groups': groups})
```

## 制作添加模块页

```python
# webadmin/urls.py
from django.urls import path
from webadmin import views

urlpatterns = [
    path('', views.index, name='webadmin_index'),
    path('add_hosts', views.add_hosts, name='add_hosts'),
    path('add_modules', views.add_modules, name='add_modules'),
]

# webadmin/views.py
from django.shortcuts import render
from webadmin.models import HostGroup, Module
... ...
def add_modules(request):
    if request.method == 'POST':
        module = request.POST.get('module').strip()  # 去除字符串两边额外的空格
        param = request.POST.get('param').strip()
        if module:  # 如果module非空
            # 创建或取出模块实例
            m = Module.objects.get_or_create(modulename=module)[0]
            if param:  # 如果param也是非空的
                m.argument_set.get_or_create(arg_text=param)

    # 在数据库中取出所有的模块，发往前端
    modules = Module.objects.all()
    return render(request, 'webadmin/add_modules.html', {'modules': modules})

# templates/webadmin/add_modules.html
{% extends 'basic.html' %}
{% block title %}添加模块{% endblock %}
{% block content %}
    <form action="{% url 'add_modules' %}" class="form-inline h4" method="post">
        {% csrf_token %}
        <div class="form-group">
            模块: <input class="form-control" type="text" name="module">
        </div>
        <div class="form-group">
            参数: <input class="form-control" type="text" name="param">
        </div>
        <div class="form-group">
            <input class="btn btn-primary" type="submit" value="提 交">
        </div>
    </form>
    <hr>
    <table class="table table-bordered table-hover table-striped h4">
        <thead class="bg-primary">
            <tr>
                <td>模块</td>
                <td>参数</td>
            </tr>
        </thead>
        <tbody>
            {% for module in modules %}
                <tr>
                    <td>{{ module }}</td>
                    <td>
                        {% for arg in module.argument_set.all %}
                            <div>{{ arg.arg_text }}</div>
                        {% endfor %}
                    </td>
                </tr>
            {% endfor %}
        </tbody>
    </table>
{% endblock %}

# 修改index.html中添加模块的超链接
# templates/index/index.html
<a href="{% url 'add_modules' %}" target="_blank">
    <img src="{% static 'imgs/linux.jpg' %}" width="150px"><br>
    添加模块
</a>
```



