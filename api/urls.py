from django.urls import path
from .views import *

urlpatterns = [
    path('course/', CourseAPIView.as_view()),
    path('course/<int:pk>/',CourseDetail.as_view()),
    path('availablecourse/', AvailableCourseAPIView.as_view()),
    path('availablecourse/<int:pk>/', AvailableCourseDetail.as_view()),
    path('bid/',BidAPIView.as_view()),
    path('bid/<int:pk>/',BidDetail.as_view()),
    path('student/',StudentAPIView.as_view()),
    path('student/<str:username>/',StudentDetail.as_view()),
    path('professor/',ProfessorAPIView.as_view()),
    path('professor/<int:pk>/',ProfessorDetail.as_view()),
    path('student_courses/',StudentsCourses),
    path('student_courses/<int:student>/',StudentCourses),
    ]
