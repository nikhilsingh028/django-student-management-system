from django.shortcuts import render, redirect, get_object_or_404

from .models import Student, StudentProfile


# HOME PAGE
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


# ABOUT PAGE
def about(request):

    context = {
        "title": "About Us",
        "description": "We are learning Django web development."
    }

    return render(request, "students/about.html", context)


# READ: DISPLAY ALL STUDENTS
def student_list(request):

    students = Student.objects.all().order_by("id")

    context = {
        "students": students
    }

    return render(request, "students/student_list.html", context)


# READ: DISPLAY ONE STUDENT
def student_detail(request, student_id):

    student = get_object_or_404(Student, id=student_id)

    context = {
        "student": student
    }

    return render(
        request,
        "students/student_detail.html",
        context
    )


# CREATE: ADD A STUDENT
def student_create(request):

    if request.method == "POST":

        name = request.POST.get("name", "").strip()
        email = request.POST.get("email", "").strip()
        age = request.POST.get("age", "").strip()
        course = request.POST.get("course", "").strip()

        if not all([name, email, age, course]):
            return render(
                request,
                "students/student_form.html",
                {"error": "Please fill in all fields."}
            )

        if not age.isdigit():
            return render(
                request,
                "students/student_form.html",
                {"error": "Age must be a positive whole number."}
            )

        if Student.objects.filter(email=email).exists():
            return render(
                request,
                "students/student_form.html",
                {"error": "This email already exists."}
            )

        Student.objects.create(
            name=name,
            email=email,
            age=int(age),
            course=course
        )

        return redirect("student_list")

    return render(request, "students/student_form.html")


# UPDATE: EDIT A STUDENT
def student_update(request, student_id):

    student = get_object_or_404(Student, id=student_id)

    if request.method == "POST":

        name = request.POST.get("name", "").strip()
        email = request.POST.get("email", "").strip()
        age = request.POST.get("age", "").strip()
        course = request.POST.get("course", "").strip()

        if not all([name, email, age, course]):
            return render(
                request,
                "students/student_form.html",
                {
                    "student": student,
                    "error": "Please fill in all fields."
                }
            )

        if not age.isdigit():
            return render(
                request,
                "students/student_form.html",
                {
                    "student": student,
                    "error": "Age must be a positive whole number."
                }
            )

        duplicate_email = Student.objects.filter(
            email=email
        ).exclude(id=student.id).exists()

        if duplicate_email:
            return render(
                request,
                "students/student_form.html",
                {
                    "student": student,
                    "error": "This email already exists."
                }
            )

        student.name = name
        student.email = email
        student.age = int(age)
        student.course = course

        student.save()

        return redirect("student_list")

    return render(
        request,
        "students/student_form.html",
        {"student": student}
    )


# DELETE: DELETE A STUDENT
def student_delete(request, student_id):

    student = get_object_or_404(Student, id=student_id)

    if request.method == "POST":

        student.delete()

        return redirect("student_list")

    return render(
        request,
        "students/student_confirm_delete.html",
        {"student": student}
    )


# MEDIA: UPLOAD STUDENT PROFILE
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