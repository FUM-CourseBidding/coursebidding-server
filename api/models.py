from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _

class Student(AbstractUser):
    #last_semester_grade = models.PositiveSmallIntegerField(null = True)
    budget = models.PositiveSmallIntegerField(null = True)

    course_bidding_fields = ['budget']

    class Meta:
        verbose_name = _('student')
        verbose_name_plural = _('students')

    def __str__(self):
        return self.username

    class Bid(models.Model):
        course_code = models.PositiveSmallIntegerField()
        semester = models.DateField()
        value = models.PositiveSmallIntegerField()

class Course(models.Model):
    code = models.PositiveIntegerField(primary_key=True)
    group_number = models.PositiveSmallIntegerField(primary_key=True)
    semester = models.DateField()
    professor_name = models.CharField(max_length=50)
    subject = models.CharField(max_length=50)
    credit = models.PositiveSmallIntegerField()
    capacity = models.PositiveSmallIntegerField()
