from rest_framework import serializers

from users.models import UserProfile, CustomUser, Stats

class StatsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Stats
        fields = '__all__'

class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = '__all__'

class UserSerializer(serializers.ModelSerializer):
    profile = UserProfileSerializer(many=False)
    stats = StatsSerializer(many=False)
    class Meta:
        model = CustomUser
        fields = ('email','profile','stats')