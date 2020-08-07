# nsd2002-devweb-day04

## 模型操作

- 使用python shell操作模型

```python
[root@localhost mysite]# python3 manage.py shell
>>> from polls.models import Question, Choice
# 创建问题方法一：直接实例化
>>> q1 = Question(question_text='出游去哪玩？', pub_date='2020-07-30 12:00:00')
>>> q1.save()
>>> q1.id
3
>>> q1.question_text
'出游去哪玩？'
>>> q1.pub_date
'2020-07-30 12:00:00'

# 创建问题方法二：使用objects管理器
# 每个模型都有一个名为objects的管理器，通过它，可以对模型进行增删改查
>>> result1 = Question.objects.get_or_create(question_text='散伙饭哪里吃？', pub_date='2020-08-10')
>>> result1  # result是一个元组：(问题实例，True/False)
(<Question: 问题:散伙饭哪里吃？>, True)  # 创建成功为True
>>> result1 = Question.objects.get_or_create(question_text='散伙饭哪里吃？', pub_date='2020-08-10')
>>> result1
(<Question: 问题:散伙饭哪里吃？>, False)  # 创建失败为False
>>> q2 = result1[0]  # 在元组中取出问题实例
>>> q2
<Question: 问题:散伙饭哪里吃？>

# 创建选项方法一：创建实例
>>> c1 = Choice(choice_text='北戴河', question=q1)
>>> c1.save()
>>> c1.id
5
>>> c1.choice_text
'北戴河'
>>> c1.votes
0
>>> c1.question
<Question: 问题:出游去哪玩？>

# 创建选项方法二：使用objects管理器
>>> c2 = Choice.objects.get_or_create(choice_text='杭州', question=q1)[0]
>>> c2
<Choice: 问题:出游去哪玩？=>选项:杭州>

# 创建选项方法三：通过问题实例创建选项
# 问题和选项之间有主外键约束，一个问题可以对应多个选项，问题的选项集就是：类名_set（小写）；选项的类名叫Choice，那么问题的选项集就叫choice_set。choice_set与objects管理器类似，通过它，可以为具体的问题选项做增删改查。
>>> result2 = q1.choice_set.get_or_create(choice_text='广州')
>>> result2
(<Choice: 问题:出游去哪玩？=>选项:广州>, True)
>>> c3 = result2[0]
>>> c3
<Choice: 问题:出游去哪玩？=>选项:广州>

# 查询所有问题，返回所有问题实例构成的查询集。查询集与列表类似，支持下标操作、循环遍历。
>>> qset1 = Question.objects.all()
>>> for q in qset1:
...   print(q.question_text, q.pub_date)

# 取出全部问题，根据时间升序排列
>>> qset2 = Question.objects.order_by('pub_date')
>>> for q in qset2:
...   print(q.question_text, q.pub_date)

# 取出全部问题，根据时间降序排列
>>> qset3 = Question.objects.order_by('-pub_date')
>>> for q in qset3:
...   print(q.question_text, q.pub_date)

# 取出指定条件的问题。get方法要求必须返回一个结果，0个或多个都将报错
>>> Question.objects.get(id=10)  # 报错，不存在
polls.models.Question.DoesNotExist: Question matching query does not exist.
>>> Question.objects.get(id__gt=1)  # 报错，满足问题的条件太多
polls.models.Question.MultipleObjectsReturned: get() returned more than one Question -- it returned 3!
>>> q1 = Question.objects.get(id=1)
>>> q1
<Question: 问题:你期待工资有多少？>
# 取出指定条件的问题。filter方法可以返回0到多个结果构成的查询集
>>> qset1 = Question.objects.filter(id=10)
>>> qset1
<QuerySet []>
>>> qset1 = Question.objects.filter(id__lt=10)
>>> qset1
<QuerySet [<Question: 问题:你期待工资有多少？>, <Question: 问题:你期待进入哪家公司？>, <Question: 问题:散伙饭哪里吃？>]>

# django的查询条件使用灵活的双下划线来表示属性或方法
# https://docs.djangoproject.com/zh-hans/2.2/
# https://docs.djangoproject.com/zh-hans/3.1/ref/models/querysets/#field-lookups
# 严格匹配
>>> Question.objects.filter(id__exact=1)
<QuerySet [<Question: 问题:你期待工资有多少？>]>
# 上面可以简写成
>>> Question.objects.filter(id=1)
# 大于
>>> Question.objects.filter(id__gt=1)
# 大于等于
>>> Question.objects.filter(id__gte=1)
# 小于
>>> Question.objects.filter(id__lt=1)
# 小于等于
>>> Question.objects.filter(id__lte=1)
# 不等于，使用exclude方法，exclude是排除的意思
>>> Question.objects.exclude(id=1)
# 关键字中包含某些字符
>>> Question.objects.filter(question_text__contains='工资')
# 关键字以某些字符开头
>>> Question.objects.filter(question_text__startswith='散伙饭')
# 关键字以某些字符结尾
>>> Question.objects.filter(question_text__endswith='?')

# 更新，只要对实例重新赋值即可
>>> q1 = Question.objects.get(question_text__contains='工资')
>>> q1
<Question: 问题:你期待工资有多少？>
>>> q1.question_text = q1.question_text.replace('工资', '月薪')
>>> q1.save()

# 删除
>>> q2 = Question.objects.get(id=5)
>>> q2
<Question: 问题:How are you?>
>>> q2.delete()

# 查询时的注意事项：在mysite/settings.py中，如果USE_TZ = True，mysql不识别django的时区设置，所以在过滤月份时不正常。可以把USE_TZ改为False
# mysite/settings.py
... ...
USE_TZ = False
... ...
[root@localhost mysite]# python3 manage.py shell
>>> from polls.models import Question, Choice
>>> Question.objects.filter(pub_date__month=8)
```

## 完善投票首页

```python
# 修改函数
# polls/views.py
from django.shortcuts import render
from polls.models import Question
... ...
def index(request):
    # 取出所有的问题，除序排列
    questions = Question.objects.order_by('-pub_date')
    # index函数通过render函数找到一个网页模板文件，返回给客户端
    return render(request, 'index.html', {'questions': questions})
... ...

# 在网页中展示问题
# 在网页模模板中，写在{}中间的内容是模板语法，在外面的是html语法内容
# templates/index.html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>投票首页</title>
</head>
<body>
<h1>投票首页</h1>
<ol>
    {% for question in questions %}
        <li>
{#            <a href="/polls/{{ question.id }}">#}
            <a href="{% url 'detail' question.id %}"  target="_blank">
                {{ question.question_text }}
            </a>
            {{ question.pub_date }}
        </li>
    {% endfor %}
</ol>
</body>
</html>
```

## 引入bootstrap

```python
# 把devweb/day02/static拷贝到polls应用下
[root@localhost mysite]# cp -r nsd2020/nsd2002/devweb/day02/static/ polls/
# 在index.html中引入bootstrap
# templates/index.html
{% load static %}
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>投票首页</title>
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <link rel="stylesheet" href="{% static 'css/bootstrap.min.css' %}">
</head>
... ...
# 重启开发服务器
[root@localhost mysite]# python3 manage.py runserver

# 修改templates/index.html
{% load static %}
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>投票首页</title>
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <link rel="stylesheet" href="{% static 'css/bootstrap.min.css' %}">
</head>
<body>
<div class="container">
    <div class="row">
        <div id="linux-carousel" class="carousel slide">
            <ol class="carousel-indicators">
                <li class="active" data-target="#linux-carousel" data-slide-to="0"></li>
                <li data-target="#linux-carousel" data-slide-to="1"></li>
                <li data-target="#linux-carousel" data-slide-to="2"></li>
            </ol>
            <div class="carousel-inner">
                <div class="item active">
                    <a href="http://www.sogou.com" target="_blank">
                        <img src="{% static 'imgs/first.jpg' %}">
                    </a>
                </div>
                <div class="item">
                    <img src="{% static 'imgs/second.jpg' %}">
                </div>
                <div class="item">
                    <img src="{% static 'imgs/third.jpg' %}">
                </div>
            </div>
            <a href="#linux-carousel" data-slide="prev" class="carousel-control left">
                <span class="glyphicon glyphicon-chevron-left"></span>
            </a>
            <a href="#linux-carousel" data-slide="next" class="carousel-control right">
                <span class="glyphicon glyphicon-chevron-right"></span>
            </a>
        </div>
    </div>
    <div class="row">
        <h1 class="text-center text-warning">投票首页</h1>
        <ol class="h4">
            {% for question in questions %}
                <li>
                    <a href="{% url 'detail' question.id %}" target="_blank">
                        {{ question.question_text }}
                    </a>
                    {{ question.pub_date }}
                </li>
            {% endfor %}
        </ol>
    </div>
    <div class="row h4 text-center">
        tedu cloud computing &copy; <a href="#">NSD2002</a>
    </div>
</div>

<script src="{% static 'js/jquery.min.js' %}"></script>
<script src="{% static 'js/bootstrap.min.js' %}"></script>
<script type="text/javascript">
    $('#linux-carousel').carousel({
        interval : 3000
    });
</script>


</body>
</html>
```

## 模板继承

- 为了使得各个页面样式相同，可以创建一个基础模板。把共性内容写到基础模板中。
- 具体的页面继承于模板，只需要把个性化内容添加到页面中即可

```python
# 复制index.html为basic.html
[root@localhost mysite]# cp templates/index.html templates/basic.html
# 修改basic.html，将个性内容删除，使用block占位
{% load static %}
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>{% block title %}{% endblock %}</title>
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <link rel="stylesheet" href="{% static 'css/bootstrap.min.css' %}">
</head>
<body>
<div class="container">
    <div class="row">
        <div id="linux-carousel" class="carousel slide">
            <ol class="carousel-indicators">
                <li class="active" data-target="#linux-carousel" data-slide-to="0"></li>
                <li data-target="#linux-carousel" data-slide-to="1"></li>
                <li data-target="#linux-carousel" data-slide-to="2"></li>
            </ol>
            <div class="carousel-inner">
                <div class="item active">
                    <a href="http://www.sogou.com" target="_blank">
                        <img src="{% static 'imgs/first.jpg' %}">
                    </a>
                </div>
                <div class="item">
                    <img src="{% static 'imgs/second.jpg' %}">
                </div>
                <div class="item">
                    <img src="{% static 'imgs/third.jpg' %}">
                </div>
            </div>
            <a href="#linux-carousel" data-slide="prev" class="carousel-control left">
                <span class="glyphicon glyphicon-chevron-left"></span>
            </a>
            <a href="#linux-carousel" data-slide="next" class="carousel-control right">
                <span class="glyphicon glyphicon-chevron-right"></span>
            </a>
        </div>
    </div>
    <div class="row">
        {% block content %}{% endblock %}
    </div>
    <div class="row h4 text-center">
        tedu cloud computing &copy; <a href="#">NSD2002</a>
    </div>
</div>

<script src="{% static 'js/jquery.min.js' %}"></script>
<script src="{% static 'js/bootstrap.min.js' %}"></script>
<script type="text/javascript">
    $('#linux-carousel').carousel({
        interval : 3000
    });
</script>

</body>
</html>

# 在index.html中，删除共性内容，把个性内容放到相应的block中
{% extends 'basic.html' %}
{% block title %}投票首页{% endblock %}
{% block content %}
    <h1 class="text-center text-warning">投票首页</h1>
    <ol class="h4">
        {% for question in questions %}
            <li>
                <a href="{% url 'detail' question.id %}" target="_blank">
                    {{ question.question_text }}
                </a>
                {{ question.pub_date }}
            </li>
        {% endfor %}
    </ol>
{% endblock %}
```

## 制作投票详情页

```python
# polls/views.py
... ...
def detail(request, qid):
    # qid用于接收来自于url的参数
    question = Question.objects.get(id=qid)
    return render(request, 'detail.html', {'question': question})
... ...

# templates/detail.html
{% extends 'basic.html' %}
{% block title %}投票详情{% endblock %}
{% block content %}
    <h1 class="text-center text-warning">{{ question.id }}号问题投票详情</h1>
    <h2>{{ question.question_text }}</h2>
    <form class="h4" action="" method="post">
        {% csrf_token %}   {% comment %}安全选项，防止跨站攻击{% endcomment %}
        {% for choice in question.choice_set.all %}
            <div class="checkbox">
                <label>
                    <input type="radio" name="choice_id" value="{{ choice.id }}">
                    {{ choice.choice_text }}
                </label>
            </div>
        {% endfor %}
        <div class="form-group">
            <input class="btn btn-primary" type="submit" value="提 交">
        </div>
    </form>
{% endblock %}
```





```python


```





