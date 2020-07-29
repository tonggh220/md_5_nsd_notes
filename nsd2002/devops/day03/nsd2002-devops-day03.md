# nsd2002-devops-day03

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
"set cursorline
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

