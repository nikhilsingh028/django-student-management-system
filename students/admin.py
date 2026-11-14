from django.contrib import admin
from .models import StudentUpload
from .models import Student


@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):

    list_display = (
        "id",
        "name",
        "email",
        "age",
        "course",
        "phone",
        "created_at"
    )

    search_fields = (
        "name",
        "email",
        "course"
    )

    list_filter = (
        "course",
        "age"
    )

    ordering = ("-created_at",)

    readonly_fields = ("created_at",)

    list_per_page = 10



admin.site.register(StudentUpload)    