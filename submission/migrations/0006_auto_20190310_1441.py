# Generated by Django 2.1.7 on 2019-03-10 14:41

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('submission', '0005_auto_20190310_1431'),
    ]

    operations = [
        migrations.AlterField(
            model_name='submission',
            name='runid',
            field=models.CharField(help_text='运行ID', max_length=128, null=True, verbose_name='运行ID'),
        ),
    ]
