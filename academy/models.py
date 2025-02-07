from django.db import models

# Create your models here.
class Course(models.Model):
    name = models.CharField(max_length=255, unique=True)

    def __str__(self):
        return self.name

class Student(models.Model):
    full_name = models.CharField(max_length=255)
    mobile = models.CharField(max_length=15, unique=True)
    national_code = models.CharField(max_length=10, unique=True)
    age = models.IntegerField()
    job = models.CharField(max_length=255, blank=True, null=True)
    registered_course = models.ForeignKey(Course, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.full_name} - {self.registered_course.name}"
