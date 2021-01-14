from django.shortcuts import render
from rest_framework import generics, permissions
from .permissions import *
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import *
from .serializers import *


class CourseAPIView(generics.ListCreateAPIView):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer


class CourseDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAdminOrReadOnlyStudent,)
    queryset = Course.objects.all()
    serializer_class = CourseSerializer


class AvailableCourseAPIView(generics.ListCreateAPIView):
    queryset = AvailableCourse.objects.all()
    serializer_class = AvailableCourseSerializer


class AvailableCourseDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAdminOrReadOnlyStudent,)
    queryset = AvailableCourse.objects.all()
    serializer_class = AvailableCourseSerializer


class ProfessorAPIView(generics.ListCreateAPIView):
    queryset = Professor.objects.all()
    serializer_class = ProfessorSerializer


class ProfessorDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAdminOrReadOnlyStudent,)
    queryset = Professor.objects.all()
    serializer_class = ProfessorSerializer


class StudentAPIView(generics.ListCreateAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer


class StudentDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (IsTheStudent,)
    queryset = Student.objects.all()
    serializer_class = StudentSerializer


class BidAPIView(APIView):
    permission_classes = (BidTheStudent,)
    def get(self, request):
        bids = Bid.objects.all()
        serializer = BidSerializer(bids, many=True)
        return Response({"bids": serializer.data})

    def post(self, request):
        bid = request.data.get('bid')
        serializer = BidSerializer(data=bid)
        if (serializer.is_valid()):
            serializer.save()

        return Response({"errors": serializer.errors})
