from django.urls import path
from . import views


urlpatterns = [

    path("", views.home, name="home"),

    path("about/", views.about, name="about"),

    # READ
    path(
        "students/",
        views.student_list,
        name="student_list"
    ),

    path(
        "student/<int:student_id>/",
        views.student_detail,
        name="student_detail"
    ),

    # CREATE
    path(
        "students/add/",
        views.student_create,
        name="student_create"
    ),

    # UPDATE
    path(
        "students/<int:student_id>/edit/",
        views.student_update,
        name="student_update"
    ),

    # DELETE
    path(
        "students/<int:student_id>/delete/",
        views.student_delete,
        name="student_delete"
    ),

    # MEDIA
    path(
        "upload-profile/",
        views.upload_profile,
        name="upload_profile"
    ),

]