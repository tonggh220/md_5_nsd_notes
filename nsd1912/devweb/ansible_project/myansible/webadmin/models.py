from django.db import models

class HostGroup(models.Model):
    groupname = models.CharField(max_length=50)

    def __str__(self):
        return self.groupname

class Host(models.Model):
    hostname = models.CharField(max_length=50)
    ip_addr = models.CharField(max_length=15)
    group = models.ForeignKey(HostGroup)

    def __str__(self):
        return "%s=>%s:%s" % (self.group, self.hostname, self.ip_addr)

class Module(models.Model):
    modulename = models.CharField(max_length=50)

    def __str__(self):
        return self.modulename

class Argument(models.Model):
    arg_text = models.CharField(max_length=100)
    module = models.ForeignKey(Module)

    def __str__(self):
        return "%s=>[%s]" % (self.module, self.arg_text)
