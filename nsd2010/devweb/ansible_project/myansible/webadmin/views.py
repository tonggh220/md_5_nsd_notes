from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'webadmin/index.html')

def add_hosts(request):
    return render(request, 'webadmin/add_hosts.html')
