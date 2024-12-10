from django.urls import path 
from . import views 

urlpatterns = [ 
    path('register/', views.RegisterApi.as_view(), name='register'),
    path('verify/<uuid:token>/', views.VerifyEmailApi.as_view(), name='verify_email'),
    path('request-password-reset/', views.RequestPasswordResetApi.as_view(),name='request-password-reset'),
    path('reset-password/<str:token>/', views.ResetPasswordApi.as_view(), name='reset-password'),
] 