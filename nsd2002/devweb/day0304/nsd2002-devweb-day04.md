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

```



```python

```





