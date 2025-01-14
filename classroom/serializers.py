from rest_framework import serializers
from .models import Classroom
from user.models import User

class ClassroomSerializer(serializers.ModelSerializer):
    # created_by = serializers.PrimaryKeyRelatedField(queryset=User.objects.all(), write_only=True)

    class Meta:
        model = Classroom
        fields = ['id','room_number','total_seat','created_by']