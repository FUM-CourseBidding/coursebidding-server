from django.urls import path
from .views import *

urlpatterns = [
    path('course/', CourseAPIView.as_view()),
    path('availablecourse/', AvailableCourseAPIView.as_view()),
    path('bid/',BidAPIView.as_view()),
    path('student/',StudentAPIView.as_view()),
    path('professor/',ProfessorAPIView.as_view()),
    ]
