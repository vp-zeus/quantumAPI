from rest_framework import serializers

from walk_in.serializers import RoleSerializer
from .models import User,Profile

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'

class RestrictedUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id','email']
class ProfileSerializer(serializers.ModelSerializer):
    user = RestrictedUserSerializer()
    preferred_roles = RoleSerializer(many=True)
    class Meta:
        model = Profile
        fields = '__all__'
