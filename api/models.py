from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _
from api.binding_rules import rules

class Student(AbstractUser):
    
    budget = models.PositiveSmallIntegerField(default=100)

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
class Course(models.Model):
    subject = models.CharField(max_length=50)
    unit = models.PositiveSmallIntegerField(default=3)
    semester = models.CharField(max_length=50)
    professor = models.CharField(max_length=50)
    code = models.CharField(max_length=50)
    capacity = models.PositiveSmallIntegerField(default=0)
    session1 = models.ForeignKey(Session,null=True,on_delete=models.CASCADE,related_name="Session1_set")
    session2 = models.ForeignKey(Session,null=True,on_delete=models.CASCADE,default=None,related_name="Session2_set")
    exam = models.ForeignKey(Session,null=True,on_delete=models.CASCADE,default=None,related_name="Exam_set")
    def __str__(self):
        return f'{self.course}-{self.professor}-{self.code}'
class Bid(models.Model):
    course = models.ForeignKey(Course,null=True,on_delete=models.CASCADE)
    student = models.ForeignKey(Student,null=True,on_delete=models.CASCADE)
    value = models.PositiveSmallIntegerField()
    def __str__(self):
        return f'{self.student}-{self.course}-{self.value}'
    

