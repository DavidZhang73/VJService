import uuid

from django.db import models


class Problem(models.Model):
    id = models.CharField('ID', primary_key=True, default=uuid.uuid1, max_length=36, help_text='ID')
    soj = models.CharField('OJ名称', max_length=128, help_text='OJ名称')
    sid = models.IntegerField('编号', help_text='编号')
    title = models.CharField('标题', max_length=128, help_text='标题')
    time_limit = models.CharField('时间限制', max_length=128, help_text='时间限制')
    memory_limit = models.CharField('内存限制', max_length=128, help_text='内存限制')
    description = models.TextField('描述', help_text='描述')
    input = models.TextField('输入', help_text='输出')
    output = models.TextField('输出', help_text='输入')
    sample_input = models.TextField('输入样例', help_text='输入样例')
    sample_output = models.TextField('输出样例', help_text='输出样例')
    source = models.TextField('来源', blank=True, help_text='来源')
    update_time = models.DateTimeField('更新时间', auto_now=True, help_text='更新时间')

    def __str__(self):
        return f'{self.soj}-{self.sid}-{self.title}'
