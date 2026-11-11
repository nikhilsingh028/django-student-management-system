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

    path(
      "contact/",
       views.contact_view,
       name="contact"
    ),

    path(
      "students/<int:student_id>/edit-form/",
       views.student_edit,
       name="student_edit_form"
    ),

    path(
     "students/add/",
      StudentCreateView.as_view(),
      name="student_create"
    ),

    path(
      "register/",
       views.register_view,
       name="register"
    ),

]