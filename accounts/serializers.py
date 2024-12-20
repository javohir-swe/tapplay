import re

from rest_framework import serializers

from django.contrib.auth import get_user_model


User = get_user_model()
class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'password']
        extra_kwargs = {
            'password': {'write_only': True},
            'username': {'required': True},
        }

    def validate_phone_number(self, phone_number):
        if phone_number:
            # Regex for validating +998XXXXXXXXX (13 characters)
            pattern = r'^\+998\d{9}$'
            if not re.match(pattern, phone_number):
                raise serializers.ValidationError(
                    'Phone number must start with +998 and contain exactly 13 characters.'
                )
        return phone_number

    def create(self, validated_data):
        user = User.objects.create_user(
            username=validated_data['username'],
            password=validated_data['password']
        )
        return user
