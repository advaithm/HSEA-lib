from django.db import models

# Create your models here.
class grade(models.Model):
    Grade = models.PositiveIntegerField()
    Section = models.CharField(max_length=1000)
    Teacher1 = models.CharField(max_length=10000)
    Teacher2 = models.CharField(max_length=10000)
    email_1 = models.EmailField()
    email_2 = models.EmailField()

class student(models.Model):
    student_grade = models.PositiveIntegerField()
    section = models.CharField(max_length=1000)
    Student_id = models.PositiveIntegerField(primary_key=True)
    Student_Name = models.CharField(max_length=100000)
    Link = models.ForeignKey(grade, on_delete=models.CASCADE)