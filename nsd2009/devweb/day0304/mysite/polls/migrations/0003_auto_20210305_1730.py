# Generated by Django 2.2.12 on 2021-03-05 17:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0002_choice'),
    ]

    operations = [
        migrations.RenameField(
            model_name='choice',
            old_name='q',
            new_name='question',
        ),
    ]
