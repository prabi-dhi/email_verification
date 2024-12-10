from django.urls import path, include
from student import views

urlpatterns = [
    path('student/', views.StudentListGetApi.as_view(), name= 'student-list'),
    path('student/<int:pk>/', views.StudentDetailGetApi.as_view(), name = 'student-detail'),
    path('student/update/<int:pk>/', views.StudentDetailUpdateApi.as_view()),
    path('student/delete/<int:pk>/', views.StudentDetailDeleteApi.as_view(), name = 'student-detail-delete'),
]
