# Generated by Django 2.1.7 on 2019-03-10 14:31

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('submission', '0004_auto_20190310_1348'),
    ]

    operations = [
        migrations.AddField(
            model_name='submission',
            name='errorinfo',
            field=models.TextField(default='', help_text='错误信息', verbose_name='错误信息'),
        ),
        migrations.AddField(
            model_name='submission',
            name='memoryused',
            field=models.CharField(default='0', help_text='运行内存', max_length=128, verbose_name='运行内存'),
        ),
        migrations.AddField(
            model_name='submission',
            name='runid',
            field=models.CharField(default='0', help_text='运行ID', max_length=128, verbose_name='运行ID'),
        ),
        migrations.AddField(
            model_name='submission',
            name='timeused',
            field=models.CharField(default='0', help_text='运行时间', max_length=128, verbose_name='运行时间'),
        ),
    ]