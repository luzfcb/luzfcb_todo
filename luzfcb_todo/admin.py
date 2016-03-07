from django.contrib import admin

from .models import TodoList, Task


class TaskInline(admin.TabularInline):
    model = Task
    extra = 1


@admin.register(TodoList)
class TodoAdmin(admin.ModelAdmin):
    inlines = [TaskInline]


@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    pass
