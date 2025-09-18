from django.contrib import admin

class TaskAdmin(admin.ModelAdmin):
    readonly_fields = ('created_at',)

# Register your models here.
from .models import Task
admin.site.register(Task, TaskAdmin)