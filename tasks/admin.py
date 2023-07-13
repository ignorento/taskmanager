from django.contrib import admin
from tasks.models import TaskModel

@admin.register(TaskModel)
class TaskModelAdmin(admin.ModelAdmin):
    ...
