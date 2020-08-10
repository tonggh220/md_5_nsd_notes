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

## 制作执行任务页

```python
# webadmin/urls.py
... ...
    path('tasks', views.tasks, name='tasks'),
... ...

# webadmin/views.py
from webadmin.models import HostGroup, Module, Host
... ...
def tasks(request):
    hosts = Host.objects.all()
    groups = HostGroup.objects.all()
    modules = Module.objects.all()
    context = {'hosts': hosts, 'groups': groups, 'modules': modules}
    return render(request, 'webadmin/tasks.html', context)

# templates/webadmin/tasks.html
{% extends 'basic.html' %}
{% block title %}执行任务{% endblock %}
{% block content %}
    <ul class="nav nav-tabs h4">
        <li class="active">
            <a href="#server" data-toggle="tab">主机</a>
        </li>
        <li>
            <a href="#servers" data-toggle="tab">主机组</a>
        </li>
    </ul>
    <form action="{% url 'tasks' %}" method="post">
        {% csrf_token %}
        <div class="h4 tab-content">
            <div class="tab-pane active fade in" id="server">
                <select class="form-control" name="ip">
                    <option value="">无</option>
                    {% for host in hosts %}
                        <option value="{{ host.ip_addr }}">
                            {{ host.hostname }}:{{ host.ip_addr }}
                        </option>
                    {% endfor %}
                </select>
            </div>
            <div class="tab-pane fade" id="servers">
                <select class="form-control" name="hostgroup">
                    <option value="">无</option>
                    {% for group in groups %}
                        <option value="{{ group.groupname }}">
                            {{ group.groupname }}
                        </option>
                    {% endfor %}
                </select>
            </div>
        </div>
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
                        <td>
                            <label>
                                <input type="radio" name="module" value="{{ module }}">
                                {{ module }}
                            </label>
                        </td>
                        <td>
                            {% for arg in module.argument_set.all %}
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
{% endblock %}

# 将ansible课程部分的程序拷贝过来，作为模块使用
[root@localhost myansible]# cp nsd2020/nsd2002/devops/day03/adhoc2.py webadmin/adhoc.py

# 完善webadmin/views.py中的tasks函数
from webadmin import adhoc
... ...
def tasks(request):
    if request.method == 'POST':
        ip = request.POST.get('ip')
        group = request.POST.get('hostgroup')
        module = request.POST.get('module')
        param = request.POST.get('param')
        if ip:  # 确定是在组还是在主机上执行任务
            target = ip
        elif group:
            target = group
        else:
            target = None
        if target:  # 如果target不是None，则调用ansible执行任务
            adhoc.adhoc(['ansi_cfg/dhosts.py'], target, module, param)
            
    hosts = Host.objects.all()
    groups = HostGroup.objects.all()
    modules = Module.objects.all()
    context = {'hosts': hosts, 'groups': groups, 'modules': modules}
    return render(request, 'webadmin/tasks.html', context)
```

## 添加删除参数的功能

#### 思路

- 删除功能，需要通过一个函数来完成
- 通过访问url来实现调用函数的任务
- 可以在网页的参数后面，加一个超链接，点击超链接访问url

```python
# webadmin/urls.py
... ...
    path('del_arg/<int:arg_id>', views.del_arg, name='del_arg'),
... ...

# templates/webadmin/add_modules.html
<td>
    {% for arg in module.argument_set.all %}
        <div>
            <div class="col-md-7">{{ arg.arg_text }}</div>
            <div class="col-md-5">
                <a class="btn btn-xs btn-danger" href="{% url 'del_arg' arg.id %}">
                	delete
                </a>
            </div>
        </div>
    {% endfor %}
</td>

# webadmin/views.py
def del_arg(request, arg_id):
    arg = Argument.objects.get(id=arg_id)
    arg.delete()
    return redirect('add_modules')
```

## 部署django

### uwsgi

- WSGI：Web Server Gateway Interface，Web服务器网关接口
- uWSGI 是一个快速的、纯C语言开发的、自维护的、对开发者友好的 WSGI 服务器，旨在提供专业的 Python web应用发布和开发。
- 配置

```shell
# 安装
[root@localhost ~]# pip3 install uwsgi

# 拷贝django站点到目标位置
[root@localhost ~]# cp -r nsd2020/nsd2002/devweb/ansible_project/myansible/ /opt

# 配置uwsgi，使之可以运行django程序
[root@localhost ~]# mkdir /etc/uwsgi
[root@localhost ~]# vim /etc/uwsgi/uwsgi.ini
[uwsgi]
# 以http方式通信
http=127.0.0.1:8000
# 指定项目的工作目录
chdir=/opt/myansible
# 指定项目中的wsgi.py配置文件，位置相对于工作目录
wsgi-file=myansible/wsgi.py
# 指定启动进程的数目
process=4
# 指定每个进程启动的线程个数
threads=2
# 指定服务的pid文件
pidfile=/var/run/uwsgi.pid
# 指定日志文件位置
daemonize=/var/log/uwsgi.log
# 开启主进程管理模式
master=true

# 启动uwsgi服务
[root@localhost ~]# uwsgi --ini /etc/uwsgi/uwsgi.ini 
[root@localhost ~]# ps aux | grep wsgi
[root@localhost ~]# ss -tlnp | grep :8000
# 访问http://127.0.0.1:8000，此时样式和图片无法正常显示

# 配置nginx，使得nginx可以将请求发给uwsgi服务
# 将uwsgi服务改为socket通信方式，而不是http
[root@localhost ~]# vim /etc/uwsgi/uwsgi.ini 
[uwsgi]
# 以http方式通信
# http=127.0.0.1:8000
# 以套接字socket方式通信
socket=127.0.0.1:8000
... ...
[root@localhost ~]# ps aux | grep uwsgi  # 查看pid
[root@localhost ~]# kill -9 25080
[root@localhost ~]# uwsgi --ini /etc/uwsgi/uwsgi.ini 

# 以rpm包方式安装nginx
# EPEL官方站点：https://fedoraproject.org/wiki/EPEL/zh-cn
# 根据官方站点说明，配置epel源，只要执行以下命令即可
yum install https://dl.fedoraproject.org/pub/epel/epel-release-latest-7.noarch.rpm
[root@localhost ~]# ls /etc/yum.repos.d/epel*
/etc/yum.repos.d/epel.repo  /etc/yum.repos.d/epel-testing.repo
[root@localhost ~]# yum install -y nginx

```

