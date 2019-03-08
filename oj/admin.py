from django.contrib import admin

from . import models


# Register your models here.
@admin.register(models.OJ)
class OJAdmin(admin.ModelAdmin):
    list_display = [
        'id',
        'name',
        'start_sid',
        'end_sid'
    ]
    list_display_links = [
        'id',
        'name'
    ]
