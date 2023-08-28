from urllib import request
from rest_framework import serializers
from walk_in.models import Role
from django.contrib.auth.hashers import make_password

from walk_in.serializers import RoleSerializer
from .models import EducationalQualification, User, Profile
from common.relations import SerializablePrimaryKeyRelatedField


class RestrictedUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'email']


class ProfileSerializer(serializers.ModelSerializer):
    user = RestrictedUserSerializer(read_only=True)
    preferred_roles = SerializablePrimaryKeyRelatedField(
        queryset=Role.objects.all(), field_serializer=RoleSerializer, many=True)

    class Meta:
        model = Profile
        fields = '__all__'


class EducationalQualificationSerializer(serializers.ModelSerializer):
    class Meta:
        model = EducationalQualification
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
        data['password'] = make_password(data['password'])
        return super().to_internal_value(data)

    def create(self, validated_data):
        data = self.context['request'].data
        profile_data = data.pop('profile')

        # Create the user
        user = User(is_active=True, **validated_data)
        user.save()

        # Create the profile

        profile_serializer = ProfileSerializer(data=profile_data)
        profile_serializer.is_valid()

        print(profile_serializer.validated_data)
        profile = profile_serializer.save(user=user)

        return profile
