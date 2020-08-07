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

```



```python

```





