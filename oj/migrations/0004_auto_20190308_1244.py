# Generated by Django 2.1.7 on 2019-03-08 12:44

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('oj', '0003_auto_20190308_1024'),
    ]

    operations = [
        migrations.AlterField(
            model_name='oj',
            name='end_sid',
            field=models.IntegerField(default=1000, verbose_name='结束编号'),
        ),
        migrations.AlterField(
            model_name='oj',
            name='start_sid',
            field=models.IntegerField(default=1000, verbose_name='开始编号'),
        ),
    ]
