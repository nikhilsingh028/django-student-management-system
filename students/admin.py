from django.contrib import admin
from .models import Student, StudentProfile


@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):

    # Columns displayed in the list
    list_display = (
        "id",
        "name",
        "email",
        "age",
        "course",
        "created_at"
    )

    # Search by name and email
    search_fields = (
        "name",
        "email"
    )

    # Filters displayed on the right
    list_filter = (
        "course",
        "age"
    )

    # Default ordering
    ordering = ("name",)

    # Number of records per page
    list_per_page = 10


@admin.register(StudentProfile)
class StudentProfileAdmin(admin.ModelAdmin):

    list_display = (
        "id",
        "name"
    )

    search_fields = (
        "name",
    )


admin.site.site_header = "Student Management Admin"

admin.site.site_title = "Student Admin Portal"

admin.site.index_title = "Welcome to Student Management System"    