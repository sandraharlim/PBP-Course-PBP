# Generated by Django 3.2.8 on 2021-10-28 08:34

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
            field=models.CharField(choices=[('1', 'Monday'), ('2', 'Tuesday'), ('3', 'Wednesday'), ('4', 'Thursday'), ('5', 'Friday'), ('6', 'Saturday'), ('7', 'Sunday')], default='Monday', max_length=255),
        ),
    ]
