from django.shortcuts import render
from webadmin.models import HostGroup

def index(request):
    return render(request, 'webadmin/index.html')

def add_hosts(request):
    # print('-' * 50)
    # print(request.method)
    # print('-' * 50)
    
    groups = HostGroup.objects.all()
    return render(request, 'webadmin/add_hosts.html', {'groups': groups})
