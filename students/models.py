from django.db import models


class StudentProfile(models.Model):

    name = models.CharField(max_length=100)

    profile_picture = models.ImageField(
        upload_to="profile_pictures/",
        blank=True,
        null=True
    )

    def __str__(self):
        return self.name