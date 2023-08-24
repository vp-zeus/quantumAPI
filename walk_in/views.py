from django.shortcuts import render
from rest_framework import mixins
from rest_framework.viewsets import ReadOnlyModelViewSet, GenericViewSet
from rest_framework.permissions import IsAuthenticated
from .serializers import WalkInSerializer, VenueSerializer
from .models import WalkIn, Venue

# Create your views here.

class WalkInViewSet(ReadOnlyModelViewSet):
    serializer_class = WalkInSerializer
    queryset = WalkIn.objects.all()
    permission_classes = [IsAuthenticated]

class VenueViewSet(mixins.RetrieveModelMixin,GenericViewSet):
    serializer_class = VenueSerializer
    queryset = Venue.objects.all()

