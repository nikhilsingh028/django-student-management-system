from django.shortcuts import render
from .models import StudentProfile

def home(request):

    context = {
        "website_name": "Student Management System",
        "message": "Welcome to my Django website!",
        "name": "Nikhil",
        "age": 21,
        "course": "B.Tech CSE",
        "students": [
            "Rahul",
            "Aman",
            "Priya",
            "Neha",
            "Nikhil"
        ]
    }

    return render(request, "students/home.html", context)


def about(request):

    context = {
        "title": "About Us",
        "description": "We are learning Django web development."
    }

    return render(request, "students/about.html", context)


def student_list(request):

    students = [
        {
            "id": 1,
            "name": "Rahul",
            "course": "Python"
        },
        {
            "id": 2,
            "name": "Aman",
            "course": "Java"
        },
        {
            "id": 3,
            "name": "Priya",
            "course": "Django"
        },
        {
            "id": 4,
            "name": "Nikhil",
            "course": "DevOps"
        }
    ]

    context = {
        "students": students
    }

    return render(request, "students/student_list.html", context)


def student_detail(request, student_id):

    students = {
        1: {
            "name": "Rahul",
            "age": 21,
            "course": "Python"
        },
        2: {
            "name": "Aman",
            "age": 22,
            "course": "Java"
        },
        3: {
            "name": "Priya",
            "age": 20,
            "course": "Django"
        },
        4: {
            "name": "Nikhil",
            "age": 21,
            "course": "DevOps"
        }
    }

    student = students.get(student_id)

    if student is None:
        return render(
            request,
            "students/student_not_found.html",
            status=404
        )

    context = {
        "student": student
    }

    return render(
        request,
        "students/student_detail.html",
        context
    )


def upload_profile(request):

    message = ""

    if request.method == "POST":

        name = request.POST.get("name")

        picture = request.FILES.get("profile_picture")

        if name and picture:

            StudentProfile.objects.create(
                name=name,
                profile_picture=picture
            )

            message = "Profile uploaded successfully!"

        else:

            message = "Please enter a name and select an image."

    return render(
        request,
        "students/upload_profile.html",
        {"message": message}
    )