# Generated by Django 3.2.7 on 2021-09-15 20:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('analysis', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='jpnikkei225',
            name='time',
        ),
    ]
