from django.contrib import admin
from api.models import TaskList, Task

@admin.register(TaskList)
class TaskListAdmin(admin.ModelAdmin):
	list_display=('id', 'name', 'created_by')

@admin.register(Task)
class TasksAdmin(admin.ModelAdmin):
	list_display=('id', 'name', 'status', 'tasklist')