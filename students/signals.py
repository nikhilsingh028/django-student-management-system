from django.db.models.signals import post_save
from django.dispatch import receiver
from django.db.models.signals import m2m_changed
from .models import Student, StudentProfile


@receiver(post_save, sender=Student)
def create_student_profile(sender, instance, created, **kwargs):

    if created:
        StudentProfile.objects.create(
            student=instance
        )

        print("Student profile created automatically!")

        

@receiver(
    m2m_changed,
    sender=Student.courses.through
)
def course_changed(sender, instance, action, **kwargs):

    if action == "post_add":
        print("Course added to student!")

    elif action == "post_remove":
        print("Course removed from student!")

    elif action == "post_clear":
        print("All courses removed!")        