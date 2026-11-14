from django import forms

from .models import Student

from .models import StudentUpload

from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


class StudentForm(forms.ModelForm):

    class Meta:

        model = Student

        fields = [
            "name",
            "email",
            "age",
            "course",
            "phone"
        ]

        widgets = {

            "name": forms.TextInput(attrs={
                "class": "form-control",
                "placeholder": "Enter student name"
            }),

            "email": forms.EmailInput(attrs={
                "class": "form-control",
                "placeholder": "Enter email address"
            }),

            "age": forms.NumberInput(attrs={
                "class": "form-control",
                "placeholder": "Enter age"
            }),

            "course": forms.TextInput(attrs={
                "class": "form-control",
                "placeholder": "Enter course"
            }),

            "phone": forms.TextInput(attrs={
                "class": "form-control",
                "placeholder": "Enter phone number"
            }),

        }

class ContactForm(forms.Form):

    name = forms.CharField(
        max_length=100,
        label="Your Name"
    )

    email = forms.EmailField(
        label="Email Address"
    )

    message = forms.CharField(
        widget=forms.Textarea,
        label="Your Message"
    )  


class RegisterForm(UserCreationForm):

    email = forms.EmailField(required=True)

    class Meta:
        model = User

        fields = [
            "username",
            "email",
            "password1",
            "password2"
        ]     


class StudentUploadForm(forms.ModelForm):

    class Meta:
        model = StudentUpload

        fields = [
            "name",
            "profile_picture",
            "document"
        ]             