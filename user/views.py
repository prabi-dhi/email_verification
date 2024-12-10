from django.core.mail import send_mail
from django.conf import settings
from django.utils import timezone
from datetime import timedelta
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import User
from .models import VerificationToken
from .serializers import UserSerializer
from django.contrib.sites.shortcuts import get_current_site
from django.template.loader import render_to_string
from django.contrib.auth.tokens import default_token_generator

class RegisterView(APIView):
    def post(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            token = VerificationToken.objects.create(
                user=user,
                expires_at=timezone.now() + timedelta(hours=1)
            )
            self.send_verification_email(user, token)

            return Response({
                'message': 'User created !!. Please check email to verify.',
                'user': { 'username': user.username, 'email': user.email, 'user_type': user.user_type,}
            }, status=status.HTTP_201_CREATED)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def send_verification_email(self, user, token):
        token_str = str(token.token)
        # current_site = get_current_site(self.request)
        # verification_url = f'http://{current_site.domain}/verify/{token_str}/'
        verification_url = f'http://127.0.0.1:8000/verify/{token_str}/'

        subject = 'Verify Your Account'
        message = render_to_string(
            'email/verification_email.html',
            {
                'user': user,
                'verification_url': verification_url,
            }
        )   
        send_mail(subject, message, settings.DEFAULT_FROM_EMAIL, [user.email])

class VerifyEmailView(APIView):
    def get(self, request, token):
        try:
            token_obj = VerificationToken.objects.filter(token=token).last()
            if token_obj.is_expired():
                return Response({'error': 'Verification link expired'}, status=status.HTTP_400_BAD_REQUEST)
            user = token_obj.user
            user.is_verified = True
            user.save()
            token_obj.delete()
            return Response({'message': 'Email successfully verified!'}, status=status.HTTP_200_OK)
        except VerificationToken.DoesNotExist:
            return Response({'error': 'Invalid verification token'}, status=status.HTTP_400_BAD_REQUEST)