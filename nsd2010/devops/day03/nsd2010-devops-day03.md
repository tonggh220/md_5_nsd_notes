# nsd2010-devops-day03

[TOC]

## ansible

- 安装基于python3的ansible

```python
# 查询可用的ansible版本
[root@localhost day03]# pip3 install ansible==
# 安装ansible2.7
[root@localhost day03]# pip3 install ansible==2.7.18
```

### ansible应用

#### 配置环境

```shell
[root@localhost nsd2020]# vim ~/.vimrc
filetype plugin on
let g:pydiction_location = '/root/.vim/bundle/pydiction/complete-dict'
syntax on
set scrolloff=7
set ai
set ts=4
set et
set encoding=utf8
autocmd FileType yaml setlocal sw=2 ts=2 et ai
nnoremap <C-a> <Home>
nnoremap <C-e> <End>
nnoremap <F2> :set nu! nu?<CR>
nnoremap ; :
    
[root@localhost day03]# mkdir myansible
[root@localhost day03]# cd myansible
[root@localhost myansible]# vim ansible.cfg
[defaults]
inventory = hosts
remote_user = root
host_key_checking = no  # 不检查远程主机密钥

[root@localhost myansible]# vim hosts
[dbservers]
localhost

[webservers]
192.168.1.136

[root@localhost myansible]# ansible all --list-hosts

[root@localhost myansible]# yum install -y sshpass
[root@localhost myansible]# ansible all -m ping -k
SSH password: 
```

#### ad-hoc临时命令

```shell
# 实现免密登陆
[root@localhost myansible]# ansible all -m authorized_key -a "user=root state=present key={{lookup('file', '/root/.ssh/id_rsa.pub')}}" -k
```

#### playbook

```shell
[root@localhost myansible]# vim lamp.yml
---
- name: configure webservers
  hosts: webservers
  tasks:
    - name: install httpd
      yum:
        name: httpd
        state: present

    - name: enable httpd service
      service:
        name: httpd
        state: started
        enabled: yes

- name: configure dbservers
  hosts: dbservers
  tasks:
    - name: install mariadb-server
      yum:
        name: mariadb-server
        state: present

    - name: enable mariadb service
      service:
        name: mariadb
        state: started
        enabled: yes
# 检查语法，无误后执行
[root@localhost myansible]# ansible-playbook lamp.yml --syntax-check
[root@localhost myansible]# ansible-playbook lamp.yml 
```

## ansible编程

- adhoc模式
- http://docs.ansible.com/ -> Ansible Documentation -> 切换版本到2.7 -> 在左侧文本框中输入python api回车进行搜索：https://docs.ansible.com/ansible/2.7/dev_guide/developing_api.html?highlight=python%20api
- 将example部分的代码全部拷贝过来并运行

- 命名的元组。常规的元组通过下标访问值，命名的元组可以为下标起名，就可以通过下标的名字来访问值了。

```python
>>> from collections import namedtuple
>>> Point = namedtuple('Point', ['x', 'y', 'z'])
>>> p1 = Point(10, 20, 30)
# 命名的元组也是元组，它拥有元组的所有方法
>>> p1[0]
10
>>> p1[1:]
(20, 30)
>>> len(p1)
3
>>> p1.x   # 通过下标的名字访问值
10
>>> p1.y
20
>>> p1.z
30
```

- 将Playbook转为python数据对象

```python
---
- name: configure webservers
  hosts: webservers
  tasks:
    - name: install httpd
      yum:
        name: httpd
        state: present

    - name: enable httpd service
      service:
        name: httpd
        state: started
        enabled: yes

- name: configure dbservers
  hosts: dbservers
  tasks:
    - name: install mariadb-server
      yum:
        name: mariadb-server
        state: present

    - name: enable mariadb service
      service:
        name: mariadb
        state: started
        enabled: yes
-------------------------------------------------------
[
    {
        'name': 'configure webservers',
        'hosts': 'webservers',
        'tasks': [
            {
                'name': 'install httpd',
                'yum': {
                    'name': 'httpd',
                    'state': 'present'
                }
            },
            {
                'name': 'enable httpd service',
                'service': {
                    'name': 'httpd',
                    'state': 'started',
                    'enabled': 'yes'
                }
            }
        ]
    },
    {
        'name': 'configure dbservers',
        'hosts': 'dbservers',
        'tasks': [
            {
                'name': 'install mariadb-server',
                'yum': {
                    'name': 'mariadb-server',
                    'state': 'present'
                }
            },
            {
                'name': 'enable mariadb service',
                'service': {
                    'name': 'mariadb',
                    'state': 'started',
                    'enabled': 'yes'
                }
            }
        ]
    }
]
```

- vault password

```shell
[root@localhost myansible]# cp /etc/hosts /tmp/
# 加密
[root@localhost myansible]# ansible-vault encrypt /tmp/hosts 
New Vault password: 
Confirm New Vault password: 
[root@localhost myansible]# cat /tmp/hosts  # 已是密文
# 解密
[root@localhost myansible]# ansible-vault decrypt /tmp/hosts
Vault password: 
[root@localhost myansible]# cat /tmp/hosts  # 已是明文
```

### ansible-cmdb插件

- 用于将通过setup收集到的远程主机信息，生成web页面

```shell
# 收集远程主机信息，并保存到/tmp/out
[root@localhost myansible]# ansible all -m setup --tree /tmp/out
[root@localhost myansible]# ls /tmp/out/
192.168.1.139  localhost
# 安装ansible-cmdb
[root@localhost myansible]# pip3 install ansible-cmdb
# 通过ansible-cmdb生成web页报错，找不到模块mako
[root@localhost myansible]# ansible-cmdb /tmp/out/ > /tmp/hosts.html
# 原因是ansible-cmdb默认使用python2，需要改成python3
[root@localhost myansible]# which ansible-cmdb 
/usr/local/bin/ansible-cmdb
[root@localhost myansible]# vim $(which ansible-cmdb)
# 第14行改为python3，如下所示：
which -a python3 | while read -r TRY_PY_BIN  
# 如果使用较早版本的ansible-cmdb，则修改第8行为
PY_BIN=$(which python3)
[root@localhost myansible]# ansible-cmdb /tmp/out/ > /tmp/hosts.html
[root@localhost myansible]# firefox /tmp/hosts.html
注：如果网页按钮无法正常使用，则
[root@localhost myansible]# vim /tmp/hosts.html  # 修改
找到以下内容：
      <script type="text/javascript" charset="utf8" src="https://code.jquery.com/jquery-1.10.2.min.js"></script>
改为：
      <script type="text/javascript" charset="utf8" src="http://cdn.tmooc.cn/tmooc-web/js/jquery-2.1.1.js"></script>
... ...
```

## 编写模块

- ansible模块：https://docs.ansible.com/ansible/2.7/modules/modules_by_category.html

```shell
# 创建保存自定义模块的路径
[root@localhost myansible]# mkdir /opt/mylibs
[root@localhost myansible]# export ANSIBLE_LIBRARY=/opt/mylibs
[root@localhost myansible]# vim /opt/mylibs/rcopy.py
from ansible.module_utils.basic import AnsibleModule
import shutil

def main():
    module = AnsibleModule(
        argument_spec=dict(
            yuan=dict(required=True, type='str'),
            mubiao=dict(required=True, type='str')
        )
    )
    shutil.copy(module.params['yuan'], module.params['mubiao'])
    module.exit_json(changed=True)

if __name__ == '__main__':
    main()

[root@localhost myansible]# ansible webservers -m rcopy -a "yuan=/etc/hosts mubiao=/var/tmp/zhuji"
```

- 本地安装python模块

```shell
# 下载python的wget
[root@localhost ~]# wget https://files.pythonhosted.org/packages/47/6a/62e288da7bcda82b935ff0c6cfe542970f04e29c756b0e147251b2fb251f/wget-3.2.zip
# 安装wget到python2
[root@localhost ~]# unzip wget-3.2.zip 
[root@localhost ~]# cd wget-3.2/
[root@localhost wget-3.2]# ls
PKG-INFO  README.txt  setup.py  wget.py
[root@localhost wget-3.2]# python setup.py install


# 也可以先安装pip，再通过pip安装wget
[root@localhost ~]# wget https://files.pythonhosted.org/packages/8e/76/66066b7bc71817238924c7e4b448abdb17eb0c92d645769c223f9ace478f/pip-20.0.2.tar.gz

# pip的安装方法与安装wget方法一样
[root@localhost ~]# tar xf pip-20.0.2.tar.gz
[root@localhost ~]# cd pip-20.0.2.tar.gz
[root@localhost pip-20.0.2]# python setup.py install
# 通过pip安装wget
[root@localhost ~]# pip install wget
```

- 编写下载模块

```python
[root@localhost myansible]# vim /opt/mylibs/download.py 
from ansible.module_utils.basic import AnsibleModule
import wget

def main():
    module = AnsibleModule(
        argument_spec=dict(
            url=dict(required=True, type='str'),
            dest=dict(required=True, type='str')
        )
    )
    wget.download(module.params['url'], module.params['dest'])
    module.exit_json(changed=True)

if __name__ == '__main__':
    main()

[root@localhost myansible]# ansible webservers -m download -a "url=http://pic1.win4000.com/wallpaper/4/584a75098f57e.jpg dest=/tmp/girl.jpg"

```

提前准备jenkins: https://mirrors.tuna.tsinghua.edu.cn/jenkins/redhat-stable/jenkins-2.235.1-1.1.noarch.rpm
