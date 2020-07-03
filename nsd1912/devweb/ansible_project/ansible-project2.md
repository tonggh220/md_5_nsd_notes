# ansible-project2

## 制添加主机页

### 编写后端代码

```python
# webadmin/views.py
def add_hosts(request):
    # print('*' * 30)
    # print(dir(request))
    # print(request.method)
    # print(request.POST)
    if request.method == 'POST':
        g = request.POST.get('group').strip()
        h = request.POST.get('host').strip()
        ip = request.POST.get('ip').strip()
        if g:  # 如果g非空
            group = HostGroup.objects.get_or_create(groupname=g)[0]
            if h and ip:  # 如果h和ip也非空
                group.host_set.get_or_create(hostname=h, ip_addr=ip)

    groups = HostGroup.objects.all()
    return render(request, 'add_hosts.html', {'groups': groups})
```

## 制作添加模块页

```python
# webadmin/urls.py
    url(r'^add_modules/$', views.add_modules, name='add_modules'),

# webadmin/views.py
from webadmin.models import HostGroup, Module
... ...
def add_modules(request):
    if request.method == 'POST':
        m = request.POST.get('module').strip()
        param = request.POST.get('param').strip()
        if m:  # 如果m非空
            module = Module.objects.get_or_create(modulename=m)[0]
            if param:  # 如果param也非空
                module.argument_set.get_or_create(arg_text=param)

    modules = Module.objects.all()
    return render(request, 'add_modules.html', {'modules': modules})

# templates/add_modules.html
{% extends 'basic.html' %}
{% load static %}
{% block title %}添加模块{% endblock %}
{% block content %}
    <form action="" class="form-inline h4" method="post">
        {% csrf_token %}
        <div class="form-group">
            <label>模块：</label>
            <input class="form-control" type="text" name="module">
        </div>
        <div class="form-group">
            <label>参数：</label>
            <input class="form-control" type="text" name="param">
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
            {% for m in modules %}
                <tr>
                    <td>{{ m.modulename }}</td>
                    <td>
                        {% for arg in m.argument_set.all %}
                            <div>
                                {{ arg.arg_text }}
                            </div>
                        {% endfor %}
                    </td>
                </tr>
            {% endfor %}
        </tbody>
    </table>
{% endblock %}

# 修改templates/index.html中添加模块的超链接
            <a href="{% url 'add_modules' %}" target="_blank">
```

## 制作执行任务页

```python
# webadmin/urls.py
    url(r'^tasks/$', views.tasks, name='tasks'),

# webadmin/views.py
def tasks(request):
    hosts = Host.objects.all()
    groups = HostGroup.objects.all()
    modules = Module.objects.all()
    data = {'hosts': hosts, 'groups': groups, 'modules': modules}
    return render(request, 'tasks.html', data)

# templates/tasks.html
{% extends 'basic.html' %}
{% block title %}执行任务{% endblock %}
{% block content %}
    <div class="h4">
        <ul class="nav nav-tabs">
            <li class="active"><a href="#server" data-toggle="tab">主机</a></li>
            <li><a href="#servers" data-toggle="tab">主机组</a></li>
        </ul>
        <form action="" method="post">
            {% csrf_token %}
            <div class="tab-content" style="margin: 5px 0">
                <div class="tab-pane active fade in" id="server">
                    <select class="form-control" name="host">
                        <option value="">无</option>
                        {% for host in hosts %}
                            <option value="{{ host.ip_addr }}">{{ host.hostname }}:{{ host.ip_addr }}</option>
                        {% endfor %}
                    </select>
                </div>
                <div class="tab-pane fade" id="servers">
                    <select class="form-control" name="group">
                        <option value="">无</option>
                        {% for group in groups %}
                            <option value="{{ group.groupname }}">{{ group.groupname }}</option>
                        {% endfor %}
                    </select>
                </div>
            </div>
            <table class="table table-bordered table-striped table-hover">
                <thead class="bg-primary">
                <tr>
                    <td>模块</td>
                    <td>参数</td>
                </tr>
                </thead>
                <tbody>
                    {% for m in modules %}
                        <tr>
                            <td>
                                <div class="radio">
                                    <label>
                                        <input type="radio" name="module" value="{{ m.modulename }}">
                                        {{ m.modulename }}
                                    </label>
                                </div>
                            </td>
                            <td>
                                {% for arg in m.argument_set.all %}
                                    <div class="radio">
                                        <label>
                                            <input type="radio" name="param" value="{{ arg.arg_text }}">
                                            {{ arg.arg_text }}
                                        </label>
                                    </div>
                                {% endfor %}
                            </td>
                        </tr>
                    {% endfor %}
                </tbody>
            </table>
            <div class="form-group text-center">
                <input class="btn btn-primary" type="submit" value="提 交">
                <input class="btn btn-primary" type="reset" value="重 置">
            </div>
        </form>
    </div>
{% endblock %}

# teplates/index.html  修改执行务的超链接
            <a href="{% url 'tasks' %}" target="_blank">
```

#### 完成执行任务的功能

```python
# 将devops/day03/adhoc2.py拷贝过来，改名为adhoc.py
[root@db1 myansible]# cp /root/nsd2019/nsd1912/devops/day03/adhoc2.py webadmin/adhoc.py
[root@db1 myansible]# vim webadmin/adhoc.py
            # dict(action=dict(module='debug', args=dict(msg='{{shell_out.stdout}}')))

# 完成tasks函数
# webadmin/views.py
from webadmin.adhoc import adhoc
... ...

def tasks(request):
    if request.method == 'POST':
        host = request.POST.get('host')
        group = request.POST.get('group')
        module = request.POST.get('module')
        param = request.POST.get('param')
        if group:  # 如果group非空
            target = group
        elif host:
            target = host
        else:
            target = None  # 如果用户没有选择目标，则为None

        if target and module and param:  # 如果这三项都是非空的
            adhoc(['ansi_cfg/dhosts.py'], target, module, param)

    hosts = Host.objects.all()
    groups = HostGroup.objects.all()
    modules = Module.objects.all()
    data = {'hosts': hosts, 'groups': groups, 'modules': modules}
    return render(request, 'tasks.html', data)

```

## 删除参数功能

- 删除数据可以通过相关的函数完成
- 在django中，访问url实现对函数的调用
- 可以在选项后面增加一个超链接，用于访问url

```python
# webadmin/urls.py
... ...
    url(r'^/del_arg/(\d+)/$', views.del_arg, name='del_arg'),
... ...

# webadmin/views.py
from django.shortcuts import render, redirect
from webadmin.models import HostGroup, Module, Host, Argument
.. ...
def del_arg(request, arg_id):
    arg = Argument.objects.get(id=arg_id)
    arg.delete()
    # 岫除参数后，跳转到add_modules页面
    return redirect('add_modules')

# templates/add_modules.html
... ...
<td>
    {% for arg in module.argument_set.all %}
        <div class="row">
            <div class="col-sm-7">{{ arg.arg_text }}</div>
            <div class="col-sm-5">
                <a class="btn btn-danger btn-xs" href="{% url 'del_arg' arg.id %}">
                delete
                </a>
            </div>
        </div>
    {% endfor %}
</td>
... ...
```

