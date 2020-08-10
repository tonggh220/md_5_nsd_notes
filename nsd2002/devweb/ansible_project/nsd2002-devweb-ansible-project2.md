# nsd2002-devweb-ansible-project2

## 实现添加主机功能

- 添加主机的url是http://127.0.0.1:9000/webadmin/add_hosts，该url也能展示web页面
  - 该url对应的函数就应该能接收两种请求，一种为get，一种为Post

```python
# 修改templates/webadmin/add_hosts.html，将表单的方法改为post
    <form action="" class="form-inline h4" method="post">
        {% csrf_token %}
        ... ...
    </form>

# 修改视图函数，判断如果request.method是POST，则取出表单提交的数据。并在数据库中添加相应的条目
# 函数的request参数有一个名为method的属性，记录了http的方法是什么
# webadmin/views.py

```



