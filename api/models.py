from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _

class Student(AbstractUser):
    #last_semester_grade = models.PositiveSmallIntegerField(null = True)
    budget = models.PositiveSmallIntegerField(null = True,default=100)

    course_bidding_fields = ['budget']

    class Meta:
        verbose_name = _('student')
        verbose_name_plural = _('students')
        
    def __str__(self):
        return self.username

class Professor(models.Model):
    name = models.CharField(max_length=50)
    def __str__(self):
        return self.name
    


class Course(models.Model):
    code = models.PositiveIntegerField(primary_key=True)
    subject = models.CharField(max_length=50)
    unit = models.PositiveSmallIntegerField()
    def __str__(self):
        return self.subject
class AvailableCourse(models.Model):
    semester = models.CharField(max_length=50)
    #semester is stored like XY-Z where XY is the year and Z
    # is either 1,2,3 for first half-year,second or summer semester
    professor = models.ForeignKey(Professor,on_delete=models.CASCADE)
    course = models.ForeignKey(Course,on_delete=models.CASCADE)
    group_number = models.PositiveSmallIntegerField()
    capacity = models.PositiveSmallIntegerField()
    def __str__(self):
        return f'{self.course}-{self.professor}'
class Bid(models.Model):
    course = models.ForeignKey(AvailableCourse,on_delete=models.CASCADE)
    student = models.ForeignKey(Student,on_delete=models.CASCADE)
    value = models.PositiveSmallIntegerField()
    def __str__(self):
        return f'{self.student}-{self.course}-{self.value}'
    

