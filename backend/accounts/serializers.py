from accounts import models
from djoser.serializers import UserCreateSerializer
from rest_framework import serializers
from django.contrib.auth import get_user_model
User = get_user_model()


class UserCreateSerializer(UserCreateSerializer):
    class Meta(UserCreateSerializer.Meta):
        model = User
        fields = ('id','email','name','password')


class UserProfileSerializer(serializers.ModelSerializer):
    """Serializes a user profile object"""

    class Meta:
        model = models.UserProfile
        fields = ('id', 'email', 'name', 'password')
        extra_kwargs = {
            'password': {
                'write_only': True,
                'style': {'input_type': 'password'}
            }
        }

    def create(self, validated_data):
        """Create and return a new user"""
        user = models.UserProfile.objects.create_user(
            email=validated_data['email'],
            name=validated_data['name'],
            password=validated_data['password']
        )

        return user

    def update(self, instance, validated_data):
        """Handle updating user account"""
        if 'password' in validated_data:
            password = validated_data.pop('password')
            instance.set_password(password)
 
        return super().update(instance, validated_data)   


class PatientInfoSerializer(serializers.ModelSerializer):
    """Serializes patient Info objects"""

    class Meta:  
        model = models.PatientInfo # Points this serializer to the patient info model
        fields = ('id','user_profile','inject_date', 'inject_time', 'blood_sugar_level', 'is_insulin_injected', 'quantity', 'inject_area',)
        extra_kwargs = {
            'user_profile': {
                'read_only': True,
            }
        }