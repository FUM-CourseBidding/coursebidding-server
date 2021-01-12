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
    def validate_value(self,value):
        student_id = self.initial_data['student']
        st = Student.objects.get(pk=student_id)
        if(value > st.budget):
            raise serializers.ValidationError("You only have {} coins dude.".format(st.budget))
        return value
    def create(self,validated_data):
        st = self.validated_data['student']
        st.budget -= validated_data['value']
        st.save()
        return Bid.objects.create(**validated_data)

class ProfessorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Professor
        fields = ('name',)

class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = ('username','first_name','last_name','is_staff','budget')
        
 
