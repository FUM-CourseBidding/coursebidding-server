from django.shortcuts import render
from rest_framework import generics
from .models import *
from .serializers import *

class CourseAPIView(generics.ListAPIView):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer

class AvailableCourseAPIView(generics.ListAPIView):
    queryset = AvailableCourse.objects.all()
    serializer_class = AvailableCourseSerializer

class BidAPIView(generics.ListAPIView):
    queryset = Bid.objects.all()
    serializer_class = BidSerializer

class ProfessorAPIView(generics.ListAPIView):
    queryset = Professor.objects.all()
    serializer_class = ProfessorSerializer

class StudentAPIView(generics.ListAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    

