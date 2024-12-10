from rest_framework import serializers
from .models import Teacher
from user.models import User

class TeacherSerializer(serializers.ModelSerializer):
    user_name = serializers.ReadOnlyField(source='user.username') 
    user_email = serializers.ReadOnlyField(source = 'user.email')

    class Meta:
        model = Teacher
        fields = ['teacher_name','user_name','user_email']