from django.contrib import admin
from .models import Student

@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ( 'name', 'email', 'phone', 'course')
    search_fields = ('name', 'email', 'phone', 'course')
    list_filter = ('course',)
    ordering = ('id',)
