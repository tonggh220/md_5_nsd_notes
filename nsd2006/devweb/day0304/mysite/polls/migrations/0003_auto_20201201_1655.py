# Generated by Django 2.2.12 on 2020-12-01 16:55

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
