# Generated by Django 2.1.7 on 2019-03-07 20:47

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('oj', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='oj',
            name='update_time',
            field=models.DateTimeField(auto_created=True, auto_now=True, verbose_name='更新时间'),
        ),
    ]
