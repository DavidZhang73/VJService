import uuid

from django.db import models


# Create your models here.
class OJ(models.Model):
    id = models.CharField('ID', primary_key=True, default=uuid.uuid1, max_length=36, help_text='ID')
    name = models.CharField('OJ名称', max_length=128, help_text='OJ名称')
    start_sid = models.IntegerField('开始编号', default=1000, help_text='开始编号')
    end_sid = models.IntegerField('结束编号', default=1000, help_text='结束编号')
    update_time = models.DateTimeField('更新时间', auto_now=True, auto_created=True, help_text='更新时间')

    def __str__(self):
        return f'{self.name} from {self.start_sid} to {self.end_sid}'


class Language(models.Model):
    id = models.CharField('ID', primary_key=True, default=uuid.uuid1, max_length=36, help_text='ID')
    name = models.CharField('语言名称', max_length=128, help_text='语言名称')
    code = models.CharField('语言代码', max_length=36, help_text='语言代码')
    oj = models.ForeignKey(verbose_name='OJ', to=OJ, on_delete=models.CASCADE, help_text='OJ')

    def __str__(self):
        return f'{self.oj.name}-{self.name}-{self.code}'


class Account(models.Model):
    id = models.CharField('ID', primary_key=True, default=uuid.uuid1, max_length=36, help_text='ID')
    username = models.CharField('用户名', max_length=128, help_text='用户名')
    nickname = models.CharField('昵称', max_length=128, help_text='昵称')
    password = models.CharField('密码', max_length=128, help_text='密码')
    oj = models.ForeignKey(verbose_name='OJ', to=OJ, on_delete=models.CASCADE, help_text='OJ')

    def __str__(self):
        return f'{self.oj.name}-{self.username}-{self.nickname}'
