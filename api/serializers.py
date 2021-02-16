from rest_framework import serializers
from .models import *
from django.contrib.auth.hashers import make_password

class SessionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Session
        fields = ('time','day')

class CourseSerializer(serializers.ModelSerializer):
    def get_session1_detail(self,obj):
        try:
            return f'{obj.session1.day}-{obj.session1.time}'
        except:
            return ""
    def get_session2_detail(self,obj):
        try:
            return f'{obj.session2.day}-{obj.session2.time}'
        except:
            return ""
    def get_exam_detail(self,obj):
        try:
            return f'{obj.exam.day}-{obj.exam.time}'
        except:
            return ""
    
    session_1 = serializers.SerializerMethodField('get_session1_detail')
    session_2 = serializers.SerializerMethodField('get_session2_detail')
    exam_ = serializers.SerializerMethodField('get_exam_detail')
    
    class Meta:
        model = Course
        fields = ('subject','unit','semester','code','professor','capacity','session_1','session_2','exam_')
        



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

 
