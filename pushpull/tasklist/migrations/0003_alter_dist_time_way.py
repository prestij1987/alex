# Generated by Django 5.1.3 on 2024-11-09 13:26

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tasklist', '0002_dist'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dist',
            name='time_way',
            field=models.DateField(verbose_name=datetime.datetime(2024, 11, 9, 13, 26, 35, 915174)),
        ),
    ]
