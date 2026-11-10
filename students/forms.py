from django import forms

from .models import Student


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