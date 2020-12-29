from rest_framework import serializers
from .models import *
class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = ('code','subject','unit')

class AvailableCourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = AvailableCourse
        fields = ('semester','professor','course','group_number','capacity')


class BidSerializer(serializers.ModelSerializer):
    class Meta:
        model = Bid
        fields = ('course','student','value')

class ProfessorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Professor
        fields = ('name',)

class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = ('username','first_name','last_name','is_staff','budget')
        
