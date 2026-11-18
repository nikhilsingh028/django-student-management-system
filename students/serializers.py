from rest_framework import serializers
from .models import Student


class StudentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Student
        fields = "__all__"

# ModelSerializer -> It automatically creates serializer fields based on your Django model.

# class Meta -> It provides configuration information to the serializer.

# model = Student -> It tells DRF which model to use.

# fields = "__all__" -> It includes all fields from the Student model.