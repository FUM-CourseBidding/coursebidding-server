from django.shortcuts import render
from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.response import Response
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
    
class BidAPIView(APIView):
    def get(self,request):
        bids = Bid.objects.all()
        serializer = BidSerializer(bids,many=True)
        return Response({"bids":serializer.data})

    def post(self,request):
        bid = request.data.get('bid')
        serializer = BidSerializer(data=bid)
        if(serializer.is_valid()):
            serializer.save()

        return Response({"errors":serializer.errors})
