# Generated by Django 2.2.12 on 2021-01-28 16:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Choice',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('choice_text', models.CharField(max_length=200)),
                ('votes', models.IntegerField(default=0)),
                ('q', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='polls.Question')),
            ],
        ),
    ]
