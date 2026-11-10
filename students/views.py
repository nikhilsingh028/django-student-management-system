from django.shortcuts import render, redirect, get_object_or_404
from django.db.models import Q

from .models import Student
from .forms import StudentForm


# DASHBOARD
def dashboard(request):

    total_students = Student.objects.count()

    recent_students = Student.objects.order_by("-created_at")[:5]

    context = {
        "total_students": total_students,
        "recent_students": recent_students
    }

    return render(request, "students/dashboard.html", context)


# READ: DISPLAY ALL STUDENTS + SEARCH
def student_list(request):

    query = request.GET.get("q", "")

    students = Student.objects.all().order_by("-created_at")

    if query:
        students = students.filter(
            Q(name__icontains=query) |
            Q(email__icontains=query) |
            Q(course__icontains=query)
        )

    context = {
        "students": students,
        "query": query
    }

    return render(request, "students/student_list.html", context)


# CREATE: ADD STUDENT
def student_create(request):

    if request.method == "POST":

        form = StudentForm(request.POST)

        if form.is_valid():

            form.save()

            return redirect("student_list")

    else:

        form = StudentForm()

    return render(
        request,
        "students/student_form.html",
        {
            "form": form,
            "title": "Add New Student"
        }
    )


# READ: STUDENT DETAILS
def student_detail(request, student_id):

    student = get_object_or_404(Student, id=student_id)

    return render(
        request,
        "students/student_detail.html",
        {"student": student}
    )


# UPDATE: EDIT STUDENT
def student_update(request, student_id):

    student = get_object_or_404(Student, id=student_id)

    if request.method == "POST":

        form = StudentForm(request.POST, instance=student)

        if form.is_valid():

            form.save()

            return redirect("student_list")

    else:

        form = StudentForm(instance=student)

    return render(
        request,
        "students/student_form.html",
        {
            "form": form,
            "title": "Update Student"
        }
    )


# DELETE: DELETE STUDENT
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