# Generated by Django 5.1.3 on 2024-11-09 13:26

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.CharField(max_length=1024)),
                ('data', models.DateField(max_length=100)),
                ('itog', models.BooleanField(verbose_name=True)),
            ],
        ),
    ]