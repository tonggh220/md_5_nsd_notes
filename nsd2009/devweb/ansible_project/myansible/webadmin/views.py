from django.shortcuts import render

def index(request):
    return render(request, 'webadmin/index.html')

def add_hosts(request):
    return render(request, 'webadmin/add_hosts.html')
