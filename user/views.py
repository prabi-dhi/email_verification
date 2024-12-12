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
# from django.contrib.sites.shortcuts import get_current_site
from django.template.loader import render_to_string
# from django.contrib.auth.tokens import default_token_generator
from django.shortcuts import get_object_or_404
import uuid
from .permissions import IsAdministration
from .paginations import CustomPagination

class UserListApi(APIView):
    def get(self, request):
        user = User.objects.all().order_by('id')
        paginator = CustomPagination()
        result = paginator.paginate_queryset(user, request)
        serializer = UserSerializer(result, many= True)
        return paginator.get_paginated_response(serializer.data)
        # serializer = UserSerializer(user, many=True)
        # return Response(serializer.data)
    
class UserDetailGetApi(APIView):
    def get(self, request, pk):
        user= User.objects.filter(pk=pk, is_deleted = False).last()
        serializer = UserSerializer(user)
        return Response(serializer.data)

class UserDetailUpdateApi(APIView):
    permission_classes= [IsAdministration]
    def post(self, request, pk):
        user= User.objects.filter(pk=pk, is_deleted= False).last()
        # user= get_object_or_404(User, pk=pk)
        serializer = UserSerializer(user, data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class UserDetailDeleteApi(APIView):
    permission_classes = [IsAdministration]
    def delete(self, request, pk):
        user= User.objects.filter(pk=pk, is_deleted= False).last()
        user.is_deleted = True
        user.save()
        return Response(status = status.HTTP_204_NO_CONTENT)

class RegisterApi(APIView):
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
        # current_site = get_current_site(self.request)
        # verification_url = f'http://{current_site.domain}/verify/{token_str}/'
        verification_url = f'http://127.0.0.1:8000/verify/{token.token}/'

        subject = 'Verify Your Account'
        message = render_to_string(
            'email/verification_email.html',
            {
                'user': user,
                'verification_url': verification_url,
            }
        )
        send_mail(subject, message, settings.DEFAULT_FROM_EMAIL, [user.email], html_message= message)

class VerifyEmailApi(APIView):
    def get(self, request, token):
        try:
            token_obj = VerificationToken.objects.filter(token=token).last()
            if token_obj.is_expired():
                return Response({'error': 'Verification link expired'}, status=status.HTTP_400_BAD_REQUEST)
            user = token_obj.user
            user.is_verified = True
            user.is_active = True
            user.save()
            token_obj.delete()
            return Response({'message': 'Email successfully verified!'}, status=status.HTTP_200_OK)
        except VerificationToken.DoesNotExist:
            return Response({'error': 'Invalid verification token'}, status=status.HTTP_400_BAD_REQUEST)

class RequestPasswordResetApi(APIView):
    def post(self, request):
        username = request.data.get('username')
        try:
            user = User.objects.get(username=username)
        except User.DoesNotExist:
            return Response({"error": "User with this username does not exist."}, status=status.HTTP_404_NOT_FOUND)
        reset_token = VerificationToken.objects.create(
                user=user,
                expires_at=timezone.now() + timedelta(hours=1)
            )        # token = default_token_generator.make_token(user)
        # reset_token = VerificationToken.objects.create(user=user, token=token,
        #     expires_at=timezone.now() + timedelta(hours=1)
        # )
        self.send_password_reset_email(user, reset_token)
        return Response({"message": "Check email to reset password"}, status=status.HTTP_200_OK)

    def send_password_reset_email(self, user, reset_token):
        reset_url = f'http://127.0.0.1:8000/reset-password/{reset_token.token}/'
        subject = 'Reset Your Password'
        message = render_to_string(
            'email/password_reset_email.html',
            {
                'user': user,
                'reset_url': reset_url,
            }
        )
        send_mail(subject, message, settings.DEFAULT_FROM_EMAIL, [user.email], html_message=message)

class ResetPasswordApi(APIView):
    def post(self, request, token):
        try:
            token_obj = VerificationToken.objects.filter(token=token).last()
        except VerificationToken.DoesNotExist:
            return Response({"error": "Invalid or expired token"}, status=status.HTTP_400_BAD_REQUEST)
        if token_obj.is_expired():
            return Response({"error": "Token has expired"}, status=status.HTTP_400_BAD_REQUEST)
        new_password = request.data.get('new_password')
        if not new_password:
            return Response({"error": "New password is required"}, status=status.HTTP_400_BAD_REQUEST)

        user = token_obj.user
        user.set_password(new_password)
        user.save()
        token_obj.delete()
        return Response({"message": "Password has been reset successfully!"}, status=status.HTTP_200_OK)