from django.db import models

class User(models.Model):
    username = models.CharField(max_length=254)
    password = models.CharField(max_length=254)

class Student(models.Model):
    user = models.OneToOneField(User,
        on_delete=models.PROTECT,
        blank = True,
    )
    name = models.CharField(max_length=50)
    last_semester_grade = models.PositiveSmallIntegerField()
    budget = models.PositiveSmallIntegerField()

class Bid(models.Model):
    user = models.OneToOneField(User,
        on_delete=models.CASCADE,
    )
    course_code = models.PositiveSmallIntegerField()
    semester = models.DateField()
    value = models.PositiveSmallIntegerField()

class Course(models.Model):
    semester = models.DateField()
    professor_name = models.CharField(max_length=50)
    subject = models.CharField(max_length=50)
    credit = models.PositiveSmallIntegerField()
    capacity = models.PositiveSmallIntegerField()
