from django.urls import path 
from . import views 
from .views import VerifyEmailView

urlpatterns = [ 
    path('register/', views.RegisterView.as_view(), name='register'),
    path('verify/<uuid:token>/', VerifyEmailView.as_view(), name='verify_email'),

    # path('user/logout/', views.LogoutApi.as_view()),

] 