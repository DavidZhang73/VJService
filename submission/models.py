import uuid

from django.db import models

from oj.models import OJ, Language
from problem.models import Problem


class Submission(models.Model):
    id = models.CharField('ID', primary_key=True, default=uuid.uuid1, max_length=36, help_text='ID')
    problem = models.ForeignKey(verbose_name='题目', to=Problem, on_delete=models.DO_NOTHING, help_text='题目')
    code = models.TextField('代码', help_text='代码')
    lang = models.ForeignKey(verbose_name='语言', to=Language, on_delete=models.DO_NOTHING, help_text='语言')
    status = models.CharField('状态', max_length=128, default='Queueing', help_text='状态')
    runid = models.CharField('运行ID', max_length=128, help_text='运行ID', null=True)
    timeused = models.CharField('运行时间', max_length=128, default='0', help_text='运行时间')
    memoryused = models.CharField('运行内存', max_length=128, default='0', help_text='运行内存')
    errorinfo = models.TextField('错误信息', default='', help_text='错误信息')
    submit_datetime = models.DateTimeField('提交时间', auto_now_add=True, help_text='提交时间')
    judge_datetime = models.DateTimeField('判题时间', blank=True, null=True, help_text='判题时间')

    def __str__(self):
        return f'{self.problem.soj}-{self.problem.sid}-{self.submit_datetime}'
