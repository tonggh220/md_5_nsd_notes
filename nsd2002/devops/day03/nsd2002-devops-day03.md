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

```python
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
```



#### ad-hoc临时命令



#### playbook