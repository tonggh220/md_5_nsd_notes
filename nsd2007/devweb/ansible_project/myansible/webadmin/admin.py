from django.contrib import admin
from webadmin.models import HostGroup, Host, Module, Arguement

for item in [HostGroup, Host, Module, Arguement]:
    admin.site.register(item)
