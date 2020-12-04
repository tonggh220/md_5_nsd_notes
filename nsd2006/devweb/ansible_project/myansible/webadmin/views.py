from django.shortcuts import render
from webadmin.models import HostGroup, Module, Host
from webadmin.adhoc import adhoc

def index(request):
    return render(request, 'webadmin/index.html')

def add_hosts(request):
    # print('-' * 50)
    # print(request.method)
    # print('-' * 50)
    if request.method == 'POST':
        group = request.POST.get('group').strip()  # 去除字符串两站空白字符
        host = request.POST.get('host').strip()
        ip = request.POST.get('ip').strip()
        if group:  # 如果group非空
            g = HostGroup.objects.get_or_create(groupname=group)[0]
            if host and ip:  # 如果host和ip也是非空的
                g.host_set.get_or_create(hostname=host, ip_addr=ip)

    groups = HostGroup.objects.all()
    return render(request, 'webadmin/add_hosts.html', {'groups': groups})

def add_modules(request):
    if request.method == 'POST':
        module = request.POST.get('module').strip()  # 去除字符串两站空白字符
        param = request.POST.get('param').strip()
        if module:  # 如果module非空
            m = Module.objects.get_or_create(modulename=module)[0]
            if param:  # 如果param也是非空的
                m.argument_set.get_or_create(arg_text=param)

    modules = Module.objects.all()
    return render(request, 'webadmin/add_modules.html', {'modules': modules})

def tasks(request):
    if request.method == 'POST':
        ip = request.POST.get('ip')
        group = request.POST.get('hostgroup')
        module = request.POST.get('module')
        param = request.POST.get('param')
        if ip:  # 如果ip非空
            target = ip
        elif group:
            target = group
        else:
            target = None
        if target:  # 如果target非空
            adhoc(['ansi_cfg/dhosts.py'], target, module, param)

    groups = HostGroup.objects.all()
    hosts = Host.objects.all()
    modules = Module.objects.all()
    context = {'groups': groups, 'hosts': hosts, 'modules': modules}
    return render(request, 'webadmin/tasks.html', context)
