from rest_framework import serializers
from user.models import User
from .models import Student

class StudentSerializer(serializers.ModelSerializer):
    user_name = serializers.ReadOnlyField(source='user.username') 
    user_email = serializers.ReadOnlyField(source = 'user.email')

    class Meta:
        model = Student
        fields = ['id', 'student_name','class_enrolled','user_name','user_email']
