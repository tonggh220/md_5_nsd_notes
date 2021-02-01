from django.shortcuts import render
from webadmin.models import HostGroup, Module

def index(request):
    return render(request, 'webadmin/index.html')

# 修改视图函数，判断如果request.method是POST，则取出表单提交的数据。并在数据库中添加相应的条目
# 函数的request参数有一个名为method的属性，记录了http的方法是什么
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
    groups = HostGroup.objects.all()
    return render(request, 'webadmin/add_hosts.html', {'groups': groups})

def add_modules(request):
    if request.method == 'POST':
        module = request.POST.get('module').strip()
        param = request.POST.get('param').strip()
        if module:  # 如果module非空
            # 创建或取出模块实例
            m = Module.objects.get_or_create(modulename=module)[0]
            if param:
                m.argument_set.get_or_create(arg_text=param)
    modules = Module.objects.all()
    return render(request, 'webadmin/add_modules.html', {'modules': modules})
