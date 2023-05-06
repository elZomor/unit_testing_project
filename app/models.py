from django.db import models
from enum import Enum


class GenderEnum(Enum):
    MALE = "MALE"
    FEMALE = "FEMALE"

    @classmethod
    def choices(cls):
        return tuple((item.name, item.value) for item in cls)


class Student(models.Model):
    name = models.CharField(max_length=200)
    gender = models.CharField(max_length=10, choices=GenderEnum.choices())


class Mobile(models.Model):
    student = models.ForeignKey("app.Student", on_delete=models.CASCADE)
    mobile = models.CharField(max_length=20)


class Course(models.Model):
    name = models.CharField(max_length=200)
    students = models.ManyToManyField("app.Student")
