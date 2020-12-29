from django.shortcuts import render
from rest_framework import generics
from .models import *
from .serializers import *

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

class BidAPIView(generics.ListCreateAPIView):
    queryset = Bid.objects.all()
    serializer_class = BidSerializer
class BidDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Bid.objects.all()
    serializer_class = BidSerializer

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
    

