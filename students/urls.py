from django.contrib import admin
from django.urls import path, include
from . import views
from .views import StudentListView


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
      "register/",
       views.register_view,
       name="register"
    ),

    path("session/create/", views.create_session, name="create_session"),
    path("session/read/", views.read_session, name="read_session"),
    path("session/update/", views.update_session, name="update_session"),
    path("session/delete-key/", views.delete_session_key, name="delete_session_key"),
    path("session/delete/", views.delete_session, name="delete_session"),
    path("session/expiry/", views.set_session_expiry, name="set_session_expiry"),


    path("cookie/create/", views.create_cookie, name="create_cookie"),
    path("cookie/read/", views.read_cookie, name="read_cookie"),
    path("cookie/update/", views.update_cookie, name="update_cookie"),
    path("cookie/delete/", views.delete_cookie, name="delete_cookie"),

    path("all-messages/", views.all_messages, name="all_messages"),


   path(
     "students/",
      StudentListView.as_view(),
      name="student_list"
    ),

]


