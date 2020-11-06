from django.shortcuts import render
from webadmin.models import HostGroup

def index(request):
    return render(request, 'webadmin/index.html')

def add_hosts(request):
    # print('-' * 30)
    # print(request.method)
    # print('-' * 30)
    if request.method == 'POST':
        group = request.POST.get('group').strip()  # 去除字符串两边额外的空格
        host = request.POST.get('host').strip()
        ip = request.POST.get('ip').strip()
        if group:  # 如果group非空
            g = HostGroup.objects.get_or_create(groupname=group)[0]
            if host and ip:   # 如果host和ip也是非空的
                g.host_set.get_or_create(hostname=host, ip_addr=ip)

    groups = HostGroup.objects.all()
    return render(request, 'webadmin/add_hosts.html', {'groups': groups})
