from django.db import models
from teacher.models import Teacher
from student.models import Student

# Create your models here.
class Subject(models.Model):
    name = models.CharField(max_length=50)
    teacher = models.ForeignKey(Teacher, null=True, blank=False, on_delete=models.SET_NULL)
    student = models.ManyToManyField(Student, blank=False)

    def __str__(self):
        return self.name