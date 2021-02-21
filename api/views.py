from django.http import HttpResponse
from django.shortcuts import render
from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import *
from .serializers import *
from . import assign
from django.views.decorators.csrf import csrf_exempt
import json
class CourseAPIView(generics.ListCreateAPIView):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer
class CourseDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer
    lookup_field = 'code'
class StudentAPIView(generics.ListCreateAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
class StudentDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    lookup_field = 'username'
class BidAPIView(APIView):
    def get(self,request):
        bids = Bid.objects.all().values()
        return Response(bids)

    def post(self,request):
        bid = request.data.copy()
        bid['student'] = request.user.pk
        b = BidSerializer(data =bid)
        b.is_valid(raise_exception=True)
        b.save()
        return Response(bid)

class StudentBidsAPIView(generics.ListCreateAPIView):
    serializer_class = BidSerializer
    def get_queryset(self):
        username = self.kwargs['username']
        st = Student.objects.filter(username=username)
        pk = st[0].pk if st else -1
        return Bid.objects.filter(student_id=pk)

class BidDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Bid.objects.all()
    serializer_class = BidSerializer
def StudentsCourses(request):
    return HttpResponse(json.dumps(assign.get_students_courses()), content_type='application/json')
def StudentCourses(request,student):
    return HttpResponse(json.dumps(assign.get_student_courses(student)), content_type='application/json')

        
class SessionAPIView(generics.ListCreateAPIView):
    queryset = Session.objects.all()
    serializer_class = SessionSerializer

