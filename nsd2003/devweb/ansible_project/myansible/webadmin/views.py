from django.shortcuts import render, redirect
from webadmin.models import HostGroup, Module, Host, Argument
from webadmin import adhoc

def index(request):
    return render(request, 'webadmin/index.html')

def add_hosts(request):
    if request.method == 'POST':
        group = request.POST.get('group').strip()
        host = request.POST.get('host').strip()
        ip = request.POST.get('ip').strip()
        if group:
            g = HostGroup.objects.get_or_create(groupname=group)[0]
            if host and ip:
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
                m.argument_set.get_or_create(arg_text=param)
    modules = Module.objects.all()
    return render(request, 'webadmin/add_modules.html', {'modules': modules})

def tasks(request):
    if request.method == 'POST':
        ip = request.POST.get('ip')
        group = request.POST.get('hostgroup')
        module = request.POST.get('module')
        param = request.POST.get('param')
        if ip:
            target = ip
        elif group:
            target = group
        else:
            target = None

        if target:
            adhoc.adhoc(['ansi_cfg/dhosts.py'], target, module, param)

    groups = HostGroup.objects.all()
    hosts = Host.objects.all()
    modules = Module.objects.all()
    context = {'groups': groups, 'hosts': hosts, 'modules': modules}
    return render(request, 'webadmin/tasks.html', context)

def del_arg(request, arg_id):
    arg = Argument.objects.get(id=arg_id)
    arg.delete()
    return redirect('add_modules')
