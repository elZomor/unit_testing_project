from django.shortcuts import render
from rest_framework import viewsets

from app.models import Student
from app.serializers import StudentSerializer


class StudentViewSet(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

