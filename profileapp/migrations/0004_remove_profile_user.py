# Generated by Django 3.0.6 on 2020-05-08 21:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('profileapp', '0003_auto_20200508_1936'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='user',
        ),
    ]
