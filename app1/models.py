from django.db import models

# Create your models here.
class CalculatedResult (models.Model):
    num1 = models.FloatField()
    num2 = models.FloatField()
    result = models.FloatField()

class Student(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    student_id = models.CharField(max_length=20)