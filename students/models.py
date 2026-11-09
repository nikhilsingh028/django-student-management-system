from django.db import models


class Student(models.Model):

    name = models.CharField(max_length=100)

    email = models.EmailField(unique=True)

    age = models.PositiveIntegerField()

    course = models.CharField(max_length=100)

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class StudentProfile(models.Model):

    name = models.CharField(max_length=100)

    profile_picture = models.ImageField(
        upload_to="profile_pictures/",
        blank=True,
        null=True
    )

    def __str__(self):
        return self.name