from rest_framework import serializers
from .models import User
# from django.contrib.auth.password_validation import validate_password
# from django.core.exceptions import ValidationError

class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, required=True, style={'input_type': 'password'})

    class Meta:
        model = User
        fields = ['username', 'email', 'password', 'user_type', 'is_verified']
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        password = validated_data.pop('password')
        user = User.objects.create(**validated_data)
        user.set_password(password)
        user.save()
        return user

    # def validate_password(self, value):
    #     try:
    #         validate_password(value)
    #     except ValidationError as e:
    #         raise serializers.ValidationError(e.messages)
    #     return value
