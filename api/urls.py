from django.urls import path
from .views import *

urlpatterns = [
    path('course/', CourseAPIView.as_view()),
    path('course/<int:pk>/',CourseDetail.as_view()),
    path('bid/',BidAPIView.as_view()),
    path('bid/<str:username>/',StudentBidsAPIView.as_view()),
    path('bid/<str:username>/<int:pk>/',BidDetail.as_view()),
    path('student/',StudentAPIView.as_view()),
    path('student/<str:username>/',StudentDetail.as_view()),
    path('student_courses/',StudentsCourses),
    path('student_courses/<int:student>/',StudentCourses),
    path('session/',SessionAPIView.as_view()),
    ]
