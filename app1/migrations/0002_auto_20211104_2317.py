# Generated by Django 3.2.8 on 2021-11-04 16:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='matkul',
            name='date',
        ),
        migrations.AddField(
            model_name='matkul',
            name='day',
            field=models.CharField(default='Monday', max_length=255),
        ),
    ]
