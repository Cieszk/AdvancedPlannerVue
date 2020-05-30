from rest_framework import serializers

from users.models import UserProfile, CustomUser, Stats

class StatsSerializer(serializers.ModelSerializer):
    """ Serialize Stats data for UserSerializer """
    class Meta:
        model = Stats
        fields = '__all__'

class UserProfileSerializer(serializers.ModelSerializer):
    """ Serialize UserProfile data for UserSerializer """
    class Meta:
        model = UserProfile
        exclude = ('user',)

class UserSerializer(serializers.ModelSerializer):
    """Serializer for full user data"""
    profile = UserProfileSerializer(many=False)
    stats = StatsSerializer(many=False)

    class Meta:
        model = CustomUser
        fields = ('id','email','profile','stats')
