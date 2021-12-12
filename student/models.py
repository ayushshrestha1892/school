from django.db import models

# Create your models here.
class Student(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    picture = models.ImageField()

    def __str__(self):
        return F"{self.first_name} {self.last_name}"