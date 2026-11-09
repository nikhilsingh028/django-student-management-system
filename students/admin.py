from django.contrib import admin
from .models import Student, StudentProfile


@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):

    list_display = ("id", "name", "email", "age", "course")

    search_fields = ("name", "email")

    list_filter = ("course",)


@admin.register(StudentProfile)
class StudentProfileAdmin(admin.ModelAdmin):

    list_display = ("id", "name")