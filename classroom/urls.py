from django.urls import path
from classroom import views

urlpatterns=[
    path('classroom/', views.ClassroomListGetApi.as_view()),
    path('classroom/add/', views.ClassroomAddApi.as_view()),
    path('classroom/<int:pk>/', views.ClassroomDetailGetApi.as_view()),
    path('classroom/update/<int:pk>/', views.ClassroomDetailUpdateApi.as_view()),
    path('classroom/delete/<int:pk>/', views.ClassroomDetailDeleteApi.as_view()),
]