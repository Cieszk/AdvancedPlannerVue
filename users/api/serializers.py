from rest_framework import serializers

from users.models import CustomUser, UserProfile

class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = ['user']

class UserSerializer(serializers.ModelSerializer):
    profile = UserProfileSerializer(required=True)
    class Meta:
        model = CustomUser
        fields = ['username', 'last_login', 'first_name', 'last_name', 'email', 'date_joined']

    def create(self, validated_data):
        # Create user
        user = CustomUser.objects.create(
            username=validated_data['username'],
            email=validated_data['email'],
            password1=validated_data['password1'],
            password2=validated_data['password2'],
        )
        