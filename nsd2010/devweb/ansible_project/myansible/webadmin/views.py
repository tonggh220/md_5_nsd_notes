from django.shortcuts import render
from webadmin.models import HostGroup

# Create your views here.
def index(request):
    return render(request, 'webadmin/index.html')

def add_hosts(request):
    groups = HostGroup.objects.all()
    return render(request, 'webadmin/add_hosts.html', {'groups': groups})
