from django.contrib import admin
from .models import Task, Status

admin.site.register(Status)



# @admin.register(Task)
# class TaskAdmin(admin.ModelAdmin):
#     list_display = ['title', 'description', 'deadline', 'status']
