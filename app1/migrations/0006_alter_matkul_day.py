# Generated by Django 3.2.8 on 2021-10-30 16:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0005_alter_matkul_day'),
    ]

    operations = [
        migrations.AlterField(
            model_name='matkul',
            name='day',
            field=models.CharField(choices=[('1', 'Monday'), ('2', 'Tuesday'), ('3', 'Wednesday'), ('4', 'Thursday'), ('5', 'Friday')], default='1', max_length=255),
        ),
    ]
