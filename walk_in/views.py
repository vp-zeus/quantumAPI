from django.shortcuts import render
from rest_framework.viewsets import ReadOnlyModelViewSet 
from .serializers import WalkInSerializer
from .models import WalkIn

# Create your views here.

class WalkInViewSet(ReadOnlyModelViewSet):
    serializer_class = WalkInSerializer
    queryset = WalkIn.objects.all()