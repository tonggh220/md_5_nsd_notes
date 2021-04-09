from django.shortcuts import render
from webadmin.models import HostGroup, Module

# Create your views here.
def index(request):
    return render(request, 'webadmin/index.html')

def add_hosts(request):
    if request.method == 'POST':  # 如果用户提交表单
        group = request.POST.get('group').strip()
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
        if module:   # 如果module非空
            m = Module.objects.get_or_create(modulename=module)[0]
            if param:  # 如果param非空
                m.argument_set.get_or_create(arg_text=param)
                
    modules = Module.objects.all()
    return render(request, 'webadmin/add_modules.html', {'modules': modules})
