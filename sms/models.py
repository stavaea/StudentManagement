from django.db import models

# Create your models here.
class Student(models.Model):
    name = models.CharField(max_length=20)
    company = models.CharField(max_length=50)
    salary = models.IntegerField()
    phone = models.CharField(max_length=20, unique=True)

class Course(models.Model):
    name = models.CharField(max_length=20)
    student = models.ManyToManyField(Student)
