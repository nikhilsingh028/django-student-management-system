from django.db.models.signals import post_save
from django.dispatch import receiver

from .models import Student, StudentProfile


@receiver(post_save, sender=Student)
def create_student_profile(sender, instance, created, **kwargs):

    if created:
        StudentProfile.objects.create(
            student=instance
        )

        print("Student profile created automatically!")