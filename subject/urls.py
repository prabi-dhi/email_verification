from django.urls import path, include
from subject import views

urlpatterns = [
    path('subject/', views.SubjectListApi.as_view()),
    path('subject/add/', views.SubjectAddApi.as_view()),
    path('subject/<int:pk>/', views.SubjectDetailGetApi.as_view()),
    path('subject/update/<int:pk>/', views.SubjectDetailUpdateApi.as_view()),
    path('subject/delete/<int:pk>/', views.SubjectDetailDeleteApi.as_view()),
]
