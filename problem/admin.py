# Register your models here.
from django.contrib import admin

from .models import Problem


@admin.register(Problem)
class ProblemAdmin(admin.ModelAdmin):
    list_display = [
        'id',
        'soj',
        'sid',
        'title',
        'update_time'
    ]
    list_display_links = [
        'id',
        'soj',
        'sid'
    ]
    list_filter = [
        'soj',
        'update_time'
    ]
    search_fields = [
        'sid',
        'sid',
        'title',
        'source'
    ]
