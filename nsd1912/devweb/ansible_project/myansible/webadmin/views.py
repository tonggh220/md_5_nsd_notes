from django.shortcuts import render, redirect
from webadmin.models import HostGroup, Module, Host, Argument
from webadmin.adhoc import adhoc


def index(request):
    return render(request, 'hosts.html')

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

def tasks(request):
    if request.method == 'POST':
        ip = request.POST.get('ip')
        group = request.POST.get('group')
        module = request.POST.get('module')
        param = request.POST.get('param')
        if ip:  # 如果ip非空
            target = ip
        elif group:  # 如果group非空
            target = group
        else:
            target = None

        if target and module and param:  # 如果这三项都非空
            adhoc(['ansi_cfg/dhosts.py'], target, module, param)

    hosts = Host.objects.all()
    groups = HostGroup.objects.all()
    modules = Module.objects.all()
    context = {'hosts': hosts, 'groups': groups, 'modules': modules}
    return render(request, 'tasks.html', context)

def del_arg(request, arg_id):
    arg = Argument.objects.get(id=arg_id)
    arg.delete()
    # 岫除参数后，跳转到add_modules页面
    return redirect('add_modules')
