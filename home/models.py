from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Person(models.Model):
   user = models.CharField(max_length = 200)
   attendance = models.IntegerField()

class Student(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username
    
class Attendance(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    date = models.DateField()
    status = models.CharField(max_length=20)

    def __str__(self):
        return self.student.user.username
    