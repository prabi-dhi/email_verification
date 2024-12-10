from django.urls import path, include
from teacher import views

urlpatterns = [
    path('teacher/', views.TeacherListApi.as_view()),
    path('teacher/<int:pk>/', views.TeacherDetailGetApi.as_view()),
    path('teacher/update/<int:pk>/', views.TeacherDetailUpdateApi.as_view()),
    path('teacher/delete/<int:pk>/', views.TeacherDetailDeleteApi.as_view()),
]