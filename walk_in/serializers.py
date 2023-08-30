from dataclasses import field
from pyexpat import model
from rest_framework import serializers

from common.relations import SerializablePrimaryKeyRelatedField
from .models import Application, TimeSlot, WalkIn, Role, Venue


class RoleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Role
        fields = '__all__'


class VenueSerializer(serializers.ModelSerializer):
    class Meta:
        model = Venue
        fields = '__all__'


class TimeSlotSerializer(serializers.ModelSerializer):
    class Meta:
        model = TimeSlot
        fields = '__all__'


class WalkInSerializer(serializers.ModelSerializer):
    roles = RoleSerializer(many=True)
    venue = VenueSerializer()
    available_time_slots = TimeSlotSerializer(many=True)

    class Meta:
        model = WalkIn
        fields = '__all__'


class ApplicationSerializer(serializers.ModelSerializer):
    walk_in = SerializablePrimaryKeyRelatedField(
        queryset=WalkIn.objects.all(),
        field_serializer=WalkInSerializer
    )
    preferred_time_slot = SerializablePrimaryKeyRelatedField(
        queryset=TimeSlot.objects.all(),
        field_serializer=TimeSlotSerializer,
    )

    preferred_roles = SerializablePrimaryKeyRelatedField(
        queryset=Role.objects.all(),
        field_serializer=RoleSerializer,
        many=True
    )

    applicant_resume = serializers.FileField()

    class Meta:
        model = Application
        fields = '__all__'
