from dataclasses import field
from pyexpat import model
from rest_framework import serializers
from .models import WalkIn, Role, Venue

class RoleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Role
        fields = '__all__'

class VenueSerializer(serializers.ModelSerializer):
    class Meta:
        model = Venue
        fields = '__all__'

class WalkInSerializer(serializers.ModelSerializer):
    roles = RoleSerializer(many=True)
    venue = VenueSerializer()
    class Meta:
        model = WalkIn
        fields = '__all__'