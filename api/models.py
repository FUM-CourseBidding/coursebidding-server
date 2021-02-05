from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _
from binding_rules import rules

class Student(AbstractUser):
    #last_semester_grade = models.PositiveSmallIntegerField(null = True)
    budget = models.PositiveSmallIntegerField(null=True, default=100)

    course_bidding_fields = ['budget']

    class Meta:
        verbose_name = _('student')
        verbose_name_plural = _('students')

    @classmethod
    def can_assign(cls, bid, student_courses): #student_courses as <QuerySet>
        aCourse_list = list(student_courses).append(bid.course)
        return all([rule(aCourse_list) for rule in rules])

    def __str__(self):
        return self.username

class Professor(models.Model):
    name = models.CharField(primary_key=True, max_length=50)
    def __str__(self):
        return self.name
    


class Course(models.Model):
    code = models.PositiveIntegerField(primary_key=True)
    subject = models.CharField(max_length=50)
    unit = models.PositiveSmallIntegerField()
    def __str__(self):
        return self.subject
class Session(models.Model):
    daysOfWeek = [(0, 'شنبه'),
    (1, 'یک شنبه'),
    (2, 'دو شنبه'),
    (3, 'سه شنبه'),
    (4, 'چهار شنبه'),
    (5, 'پنج شنبه'),
    (6, 'جمعه')
    ]
    time = models.TimeField()
    day = models.PositiveSmallIntegerField(choices = daysOfWeek)
    
    def return_as_tuple(self):
        return tuple(self.day, self.time)
class AvailableCourse(models.Model):
    semester = models.CharField(max_length=50)
    #semester is stored like XY-Z where XY is the year and Z
    # is either 1,2,3 for first half-year,second or summer semester
    professor = models.ForeignKey(Professor,on_delete=models.CASCADE)
    course = models.ForeignKey(Course,on_delete=models.CASCADE)
    group_number = models.PositiveSmallIntegerField()
    capacity = models.PositiveSmallIntegerField()
    session1 = models.ForeignKey(Session,null=True,on_delete=models.CASCADE,related_name="Session1_set")
    session2 = models.ForeignKey(Session,null=True,on_delete=models.CASCADE,default=None,related_name="Session2_set")
    def __str__(self):
        return f'{self.course}-{self.professor}'
    
class Bid(models.Model):
    course = models.ForeignKey(AvailableCourse,null=True,on_delete=models.CASCADE)
    student = models.ForeignKey(Student,null=True,on_delete=models.CASCADE)
    value = models.PositiveSmallIntegerField()
    def __str__(self):
        return f'{self.student}-{self.course}-{self.value}'
    

