import uuid

from django.db import models


class Problem(models.Model):
    id = models.CharField('ID', primary_key=True, default=uuid.uuid1, max_length=36)
    soj = models.CharField('oj名称', max_length=128)
    sid = models.IntegerField('编号')
    title = models.CharField('标题', max_length=128)
    time_limit = models.CharField('时间限制', max_length=128)
    memory_limit = models.CharField('内存限制', max_length=128)
    description = models.TextField('描述')
    input = models.TextField('输入')
    output = models.TextField('输出')
    sample_input = models.TextField('输入样例')
    sample_output = models.TextField('输出样例')
    source = models.TextField('来源', blank=True)
    update_time = models.DateTimeField('更新时间', auto_now=True)

    def __str__(self):
        return f'{self.soj}-{self.sid}-{self.title}'
