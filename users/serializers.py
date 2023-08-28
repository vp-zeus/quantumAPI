from urllib import request
from rest_framework import serializers
from walk_in.models import Role

from walk_in.serializers import RoleSerializer
from .models import User, Profile


class RestrictedUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'email']


class ProfileSerializer(serializers.ModelSerializer):
    user = RestrictedUserSerializer(read_only=True)
    preferred_roles = RoleSerializer(many=True, read_only=True)

    class Meta:
        model = Profile
        fields = '__all__'


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = '__all__'
        extra_kwargs = {
            'password': {'write_only': True}
        }

    def to_internal_value(self, data):
        data['username'] = data['email']
        return super().to_internal_value(data)

    def create(self, validated_data):
        data = self.context['request'].data
        profile_data = data.pop('profile')

        # Create the user
        user = User(is_active=True, **validated_data)
        user.save()

        # Create the profile
        preferred_roles = profile_data.pop('preferred_roles')

        profile_serializer = ProfileSerializer(data=profile_data)
        profile_serializer.is_valid()

        print(profile_serializer.validated_data)
        print(profile_serializer.errors)

        profile = profile_serializer.save(user=user)
        profile.preferred_roles.add(*preferred_roles)

        return profile
