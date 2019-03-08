import uuid

from django.db import models


# Create your models here.
class OJ(models.Model):
    id = models.CharField('ID', primary_key=True, default=uuid.uuid1, max_length=36)
    name = models.CharField('OJ名称', max_length=128)
    start_sid = models.IntegerField('开始编号', default=1000)
    end_sid = models.IntegerField('结束编号', default=1000)
    update_time = models.DateTimeField('更新时间', auto_now=True, auto_created=True)

    def __str__(self):
        return f'{self.name} from {self.start_sid} to {self.end_sid}'
