from django.urls import path, include
from . import views

urlpatterns = [
    path('grade/', views.GradeListApi.as_view()),
    path('grade/add/', views.GradeAddApi.as_view()),
    path('grade/<int:id>/', views.GradeDetailGetApi.as_view()),
    path('grade/update/<int:id>', views.GradeDetailUpdateApi.as_view()),
    path('grade/delete/<int:id>/', views.GradeDetailDeleteApi.as_view()),
]
 