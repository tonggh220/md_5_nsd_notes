from django.shortcuts import render, redirect
from webadmin.models import HostGroup, Module, Host, Arguement
from webadmin import adhoc

def index(request):
    return render(request, 'webadmin/index.html')

def add_hosts(request):
    if request.method == 'POST':
        group = request.POST.get('group').strip()  # 去除字符串两边的空格
        host = request.POST.get('host').strip()
        ip = request.POST.get('ip').strip()
        if group:  # 如果group非空，则创建或取出相关的组
            g = HostGroup.objects.get_or_create(groupname=group)[0]
            if host and ip:  # 如果host和ip也非空
                g.host_set.get_or_create(hostname=host, ip_addr=ip)

    groups = HostGroup.objects.all()
    return render(request, 'webadmin/add_hosts.html', {'groups': groups})

def add_modules(request):
    if request.method == 'POST':
        module = request.POST.get('module').strip()
        param = request.POST.get('param').strip()
        if module:
            m = Module.objects.get_or_create(modulename=module)[0]
            if param:
                m.arguement_set.get_or_create(arg_text=param)

    modules = Module.objects.all()
    return render(request, 'webadmin/add_modules.html', {'modules': modules})

def tasks(request):
    if request.method == 'POST':
        ip = request.POST.get('ip')
        group = request.POST.get('hostgroup')
        module = request.POST.get('module')
        param = request.POST.get('param')
        if ip:  # 如果ip非空则执行任务的目标就是主机
            target = ip
        elif group:
            target = group
        else:
            target = None

        # 如果target不是None，则调用ansible执行任务
        if target:
            adhoc.adhoc(['ansi_cfg/dhosts.py'], target, module, param)

    hosts = Host.objects.all()
    groups = HostGroup.objects.all()
    modules = Module.objects.all()
    context = {'hosts': hosts, 'groups': groups, 'modules': modules}
    return render(request, 'webadmin/tasks.html', context)

def del_arg(request, arg_id):
    arg = Arguement.objects.get(id=arg_id)
    arg.delete()

    return redirect('add_modules')
