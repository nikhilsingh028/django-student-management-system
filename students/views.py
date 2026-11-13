from django.shortcuts import render, redirect, get_object_or_404
from django.db.models import Q, Count, Avg

from .models import Student, Teacher
from .forms import StudentForm
from .forms import ContactForm

from django.http import HttpResponse


from django.views.generic import CreateView
from django.urls import reverse_lazy

from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView

from .forms import RegisterForm



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


def advanced_dashboard(request):

    # Q object: Python OR Java
    students = Student.objects.filter(
        Q(course="Python") | Q(course="Java")
    )

    # Aggregate: Overall statistics
    statistics = Student.objects.aggregate(
        total_students=Count("id"),
        average_age=Avg("age")
    )

    # Annotate: Number of students per teacher
    teachers = Teacher.objects.annotate(
        student_count=Count("students")
    )

    context = {
        "students": students,
        "statistics": statistics,
        "teachers": teachers,
    }

    return render(
        request,
        "students/advanced_dashboard.html",
        context
    )


def contact_view(request):

    if request.method == "POST":

        form = ContactForm(request.POST)

        if form.is_valid():

            name = form.cleaned_data["name"]
            email = form.cleaned_data["email"]
            message = form.cleaned_data["message"]

            print(name, email, message)

            return render(
                request,
                "students/contact_success.html"
            )

    else:
        form = ContactForm()

    return render(
        request,
        "students/contact.html",
        {"form": form}
    )


def clean(self):

    cleaned_data = super().clean()

    age = cleaned_data.get("age")
    course = cleaned_data.get("course")

    if age is not None and course is not None:

        if course.lower() == "python" and age < 18:

            raise forms.ValidationError(
                "Python course admission requires age 18 or above."
            )

    return cleaned_data



def student_edit(request, student_id):

    student = get_object_or_404(
        Student,
        id=student_id
    )

    if request.method == "POST":

        form = StudentAdmissionForm(
            request.POST,
            instance=student
        )

        if form.is_valid():
            form.save()
            return redirect("student_list")

    else:

        form = StudentAdmissionForm(
            instance=student
        )

    return render(
        request,
        "students/student_admission.html",
        {"form": form}
    )   

'''
class StudentCreateView(CreateView):

    model = Student

    fields = [
        "name",
        "email",
        "age",
        "course",
        "phone"
    ]

    template_name = "students/student_form.html"

    success_url = reverse_lazy("student_list")

'''



class StudentListView(LoginRequiredMixin, ListView):

    model = Student

    template_name = "students/student_list.html"

    context_object_name = "students"

    login_url = "/accounts/login/" 


def register_view(request):

    if request.method == "POST":

        form = RegisterForm(request.POST)

        if form.is_valid():

            form.save()

            return redirect("login")

    else:

        form = RegisterForm()

    return render(
        request,
        "registration/register.html",
        {"form": form}
    )       


def create_session(request):
    request.session["username"] = "nikhil"
    request.session["course"] = "Django"

    return HttpResponse("Session created successfully!")


def read_session(request):
    username = request.session.get("username", "Guest")
    course = request.session.get("course", "No course selected")

    return HttpResponse(
        f"Username: {username}, Course: {course}"
    )

def update_session(request):
    request.session["username"] = "Rahul"

    return HttpResponse("Session updated!")

def delete_session_key(request):
    request.session.pop("course", None)

    return HttpResponse("Course removed from session!")

def delete_session(request):
    request.session.flush()

    return HttpResponse("Session completely cleared!")

def set_session_expiry(request):
    request.session["username"] = "nikhil"

    # Session expires after 10 minutes
    request.session.set_expiry(600)

    return HttpResponse("Session expiry set to 10 minutes!")


from django.http import HttpResponse

def create_cookie(request):
    response = HttpResponse("Cookie created successfully!")

    response.set_cookie(
        "username",
        "nikhil",
        max_age=3600
    )

    return response

def read_cookie(request):
    username = request.COOKIES.get("username", "Guest")

    return HttpResponse(f"Welcome {username}")


def update_cookie(request):
    response = HttpResponse("Cookie updated!")

    response.set_cookie(
        "username",
        "Rahul",
        max_age=3600
    )

    return response

def delete_cookie(request):
    response = HttpResponse("Cookie deleted!")

    response.delete_cookie("username")

    return response