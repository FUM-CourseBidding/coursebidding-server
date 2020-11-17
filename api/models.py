from django.db import models


class Student(models.Model):
    username = models.CharField(max_length=50)
    password = models.CharField(max_length=50)
    name = models.CharField(max_length=50)
    last_semester_grade = models.PositiveSmallIntegerField()
    budget = models.PositiveSmallIntegerField()

class Bid(models.Model):
    username = models.CharField(max_length=50)
    course_code = models.PositiveSmallIntegerField()
    semester = models.DateField()
    value = models.PositiveSmallIntegerField()

class Course(models.Model):
    semester = models.DateField()
    code = models.AutoField()
    professor_name = models.CharField(max_length=50)
    subject = models.CharField(max_length=50)
    credit = models.PositiveSmallIntegerField()
    capacity = models.PositiveSmallIntegerField()
