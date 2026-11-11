from django.urls import path
from . import views

urlpatterns = [

    path("", views.dashboard, name="dashboard"),

    path("students/", views.student_list, name="student_list"),

    path("students/add/", views.student_create, name="student_create"),

    path(
        "students/<int:student_id>/",
        views.student_detail,
        name="student_detail"
    ),

    path(
        "students/<int:student_id>/edit/",
        views.student_update,
        name="student_update"
    ),

    path(
        "students/<int:student_id>/delete/",
        views.student_delete,
        name="student_delete"
    ),

    path(
      "advanced-dashboard/",
       views.advanced_dashboard,
       name="advanced_dashboard"
    ),

]