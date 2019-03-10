from django.contrib import admin

from .models import Submission


@admin.register(Submission)
class ProblemAdmin(admin.ModelAdmin):
    list_display = [
        'id',
        'problem',
        'status',
        'lang',
        'submit_datetime',
        'judge_datetime',
    ]
    list_display_links = [
        'id'
    ]
    list_filter = [
        'lang',
        'problem',
        'submit_datetime',
        'judge_datetime',
    ]
    search_fields = [
        'problem',
        'status',
    ]
