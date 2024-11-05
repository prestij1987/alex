# Generated by Django 5.0.6 on 2024-06-11 16:37

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('given', models.DateTimeField(blank=True, null=True)),
                ('deadline', models.DateField()),
                ('description', models.CharField(max_length=1024)),
                ('done', models.BooleanField(default=False)),
            ],
        ),
    ]
