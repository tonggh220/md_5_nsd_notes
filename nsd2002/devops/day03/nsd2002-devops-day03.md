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



#### playbook