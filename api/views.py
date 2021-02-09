from django.http import HttpResponse
from django.shortcuts import render
from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import *
from .serializers import *
from . import assign
import json
class CourseAPIView(generics.ListCreateAPIView):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer
class CourseDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer
    
class AvailableCourseAPIView(generics.ListCreateAPIView):
    queryset = AvailableCourse.objects.all()
    serializer_class = AvailableCourseSerializer
class AvailableCourseDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = AvailableCourse.objects.all()
    serializer_class = AvailableCourseSerializer
class ProfessorAPIView(generics.ListCreateAPIView):
    queryset = Professor.objects.all()
    serializer_class = ProfessorSerializer
class ProfessorDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Professor.objects.all()
    serializer_class = ProfessorSerializer

class StudentAPIView(generics.ListCreateAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
class StudentDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    lookup_field = 'username'
class BidAPIView(generics.ListCreateAPIView):
    queryset = Bid.objects.all()
    serializer_class = BidSerializer
class BidDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Bid.objects.all()
    serializer_class = BidSerializer
def StudentsCourses(request):
    return HttpResponse(json.dumps(assign.get_students_courses()), content_type='application/json')
def StudentCourses(request,student):
    return HttpResponse(json.dumps(assign.get_student_courses(student)), content_type='application/json')

        
