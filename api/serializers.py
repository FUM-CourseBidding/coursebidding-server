from rest_framework import serializers
from .models import *
from django.contrib.auth.hashers import make_password

class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = ('subject','unit','semester','code','professor','capacity','session1','session2','exam')


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


class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = ('username','password','first_name','last_name','budget')
    def update(self,instance,validated_data):
        validated_data['password'] = make_password(validated_data.get('password'))
        return super(StudentSerializer, self).update(instance,validated_data)
    def create(self, validated_data):
        validated_data['password'] = make_password(validated_data.get('password'))
        return super(StudentSerializer, self).create(validated_data)

class SessionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Session
        fields = ('time','day')
 
