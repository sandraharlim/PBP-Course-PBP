# Generated by Django 3.2.7 on 2021-11-03 12:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('to_do_list', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='todoitem',
            name='description',
        ),
    ]
