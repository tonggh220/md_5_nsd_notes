from django.shortcuts import render
from webadmin.models import HostGroup

def index(request):
    return render(request, 'webadmin/index.html')

# 修改视图函数，判断如果request.method是POST，则取出表单提交的数据。并在数据库中添加相应的条目
# 函数的request参数有一个名为method的属性，记录了http的方法是什么
def add_hosts(request):
    if request.method == 'POST':
        group = request.POST.get('group').strip()  # 去除字符串两边额外的空格
    groups = HostGroup.objects.all()
    return render(request, 'webadmin/add_hosts.html', {'groups': groups})
