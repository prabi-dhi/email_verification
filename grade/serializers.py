from rest_framework import serializers
from .models import Grade

class GradeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Grade
        fields =['student', 'subject', 'grade']