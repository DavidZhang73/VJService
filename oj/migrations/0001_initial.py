# Generated by Django 2.1.7 on 2019-03-07 20:44

import uuid

from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='OJ',
            fields=[
                ('id', models.CharField(default=uuid.uuid1, max_length=36, primary_key=True, serialize=False,
                                        verbose_name='ID')),
                ('name', models.CharField(max_length=128, verbose_name='oj名称')),
                ('start_sid', models.IntegerField(verbose_name='开始编号')),
                ('end_sid', models.IntegerField(verbose_name='结束编号')),
                ('update_time', models.DateTimeField(auto_now=True, verbose_name='更新时间')),
            ],
        ),
    ]
