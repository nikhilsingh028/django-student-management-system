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

from django import forms
from .models import StudentUpload


class StudentUploadForm(forms.ModelForm):

    class Meta:
        model = StudentUpload

        fields = [
            "name",
            "profile_picture",
            "document"
        ]

    def clean_profile_picture(self):

        image = self.cleaned_data.get("profile_picture")

        if image:

            allowed_extensions = [
                ".jpg", ".jpeg", ".png", ".webp"
            ]

            extension = "." + image.name.rsplit(".", 1)[-1].lower()

            if extension not in allowed_extensions:
                raise forms.ValidationError(
                    "Only JPG, JPEG, PNG and WebP images are allowed."
                )

            if image.size > 2 * 1024 * 1024:
                raise forms.ValidationError(
                    "Image size must be less than 2 MB."
                )

        return image

    def clean_document(self):

        document = self.cleaned_data.get("document")

        if document:

            allowed_extensions = [".pdf", ".docx"]

            extension = "." + document.name.rsplit(".", 1)[-1].lower()

            if extension not in allowed_extensions:
                raise forms.ValidationError(
                    "Only PDF and DOCX files are allowed."
                )

            if document.size > 5 * 1024 * 1024:
                raise forms.ValidationError(
                    "Document size must be less than 5 MB."
                )

        return document                