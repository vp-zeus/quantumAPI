from dataclasses import field
import profile
from urllib import request
from rest_framework import serializers
from walk_in.models import Role
from django.contrib.auth.hashers import make_password
from django.db.transaction import atomic

from walk_in.serializers import RoleSerializer
from .models import College, Degree, EducationalQualification, ProfessionalQualification, Skill, Stream, User, Profile
from common.relations import SerializablePrimaryKeyRelatedField


class RestrictedUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'email']

class DegreeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Degree
        fields = '__all__'

class StreamSerializer(serializers.ModelSerializer):
    class Meta:
        model = Stream
        fields = '__all__'

class CollegeSerializer(serializers.ModelSerializer):
    class Meta:
        model = College
        fields = '__all__'

class SkillSerializer(serializers.ModelSerializer):
    class Meta:
        model = Skill
        fields = '__all__'


class EducationalQualificationSerializer(serializers.ModelSerializer):
    degree = SerializablePrimaryKeyRelatedField(queryset=Degree.objects.all(),field_serializer=DegreeSerializer)
    stream = SerializablePrimaryKeyRelatedField(queryset=Stream.objects.all(),field_serializer=StreamSerializer)
    college = SerializablePrimaryKeyRelatedField(queryset=College.objects.all(),field_serializer=CollegeSerializer)
    class Meta:
        model = EducationalQualification
        exclude=['profile']


class ProfessionalQualificationSerializer(serializers.ModelSerializer):
    expert_skills = SerializablePrimaryKeyRelatedField(
        queryset=Skill.objects.all(),field_serializer=SkillSerializer,many=True,required=False)
    familiar_skills = SerializablePrimaryKeyRelatedField(
        queryset=Skill.objects.all(), field_serializer=SkillSerializer, many=True)

    class Meta:
        model = ProfessionalQualification
        exclude=['profile']

class ProfileSerializer(serializers.ModelSerializer):
    user = RestrictedUserSerializer(read_only=True)
    preferred_roles = SerializablePrimaryKeyRelatedField(
        queryset=Role.objects.all(), field_serializer=RoleSerializer, many=True)

    educational_qualification = EducationalQualificationSerializer(read_only=True)
    
    professional_qualification = ProfessionalQualificationSerializer(read_only=True)

    profile_pic = serializers.ImageField()

    resume = serializers.FileField()

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
        data['password'] = make_password(data['password'])
        return super().to_internal_value(data)

    @atomic
    def create(self, validated_data):
        data = self.context['data']
        profile_data = data.pop('profile')
        educational_data = profile_data.pop('educational_qualification')
        professional_data = profile_data.pop('professional_qualification')

        # Create the user
        user = User(is_active=True, **validated_data)
        user.save()

        # Create the profile

        profile_serializer = ProfileSerializer(data=profile_data)
        profile_serializer.is_valid(raise_exception=True)

        profile = profile_serializer.save(user=user)

        # Create the educational qualification

        eq_serializer = EducationalQualificationSerializer(data=educational_data)
        eq_serializer.is_valid(raise_exception=True)

        eq_serializer.save(profile=profile)

        # Create the professional qualification

        pq_serializer = ProfessionalQualificationSerializer(
            data=professional_data)
        pq_serializer.is_valid(raise_exception=True)

        pq_serializer.save(profile=profile)

        return profile
