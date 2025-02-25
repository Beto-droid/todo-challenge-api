from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User, Tasks

class TasksInline(admin.TabularInline):
    model = Tasks
    extra = 1 # add empty task
    fields = ('title', 'description', 'status', 'created_at')
    readonly_fields = ('created_at',)

@admin.register(User)
class CustomUserAdmin(UserAdmin):
    inlines = [TasksInline]

@admin.register(Tasks)
class TasksAdmin(admin.ModelAdmin):
    list_display = ('title', 'user', 'status', 'created_at')
    list_filter = ('status', 'user')
    search_fields = ('title', 'description')