from django.shortcuts import render, redirect
from webadmin.models import HostGroup, Module, Host, Argument
from webadmin import adhoc

def index(request):
    return render(request, 'webadmin/index.html')

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

def del_arg(request, arg_id):
    arg = Argument.objects.get(id=arg_id)
    arg.delete()
    return redirect('add_modules')
