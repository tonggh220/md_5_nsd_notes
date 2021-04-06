from django.db import models

class Question(models.Model):
    question_text = models.CharField(max_length=200)  # varchar(200)
    pub_date = models.DateTimeField()  # 日期时间

class Choice(models.Model):
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)
    # models.CASCADE表示级联删除，也就是在删除问题的时候，把相关的选项也一并删除
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
