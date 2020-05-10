from rest_framework import serializers
from profileapp.models import Profile


class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ['id', 'user', 'country', 'location', 'description', 'birth_date']
