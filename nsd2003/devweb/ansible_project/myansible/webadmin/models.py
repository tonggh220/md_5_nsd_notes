from django.db import models

class HostGroup(models.Model):
    groupname = models.CharField('主机组', max_length=50, unique=True)

    def __str__(self):
        return self.groupname
    
class Host(models.Model):
    hostname = models.CharField('主机', max_length=50)
    ip_addr = models.CharField('IP地址', max_length=15)
    group = models.ForeignKey(HostGroup, on_delete=models.CASCADE)

    def __str__(self):
        return "%s: %s[%s]" % (self.group, self.hostname, self.ip_addr)

class Module(models.Model):
    modulename = models.CharField('模块', max_length=50)

    def __str__(self):
        return self.modulename

class Argument(models.Model):
    arg_text = models.CharField('参数', max_length=100)
    module = models.ForeignKey(Module, on_delete=models.CASCADE)

    def __str__(self):
        return '%s: %s' % (self.module, self.arg_text)
