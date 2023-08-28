from email.mime import application
from django.shortcuts import render
from rest_framework import mixins
from rest_framework.views import APIView
from rest_framework.viewsets import ReadOnlyModelViewSet, GenericViewSet
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.parsers import JSONParser
from .serializers import ApplicationSerializer, WalkInSerializer, VenueSerializer
from .models import Application, WalkIn, Venue

# Create your views here.


class WalkInViewSet(ReadOnlyModelViewSet):
    serializer_class = WalkInSerializer
    queryset = WalkIn.objects.all()


class VenueViewSet(mixins.RetrieveModelMixin, GenericViewSet):
    serializer_class = VenueSerializer
    queryset = Venue.objects.all()


class ApplicationView(APIView):
    permission_classes = [IsAuthenticated]
    parser_classes = [JSONParser]

    def post(self, request, format=None):
        serializer = ApplicationSerializer(data=request.data)
        profile = request.user.profile
        serializer.is_valid(raise_exception=True)

        application = serializer.save(profile=profile)

        response = ApplicationSerializer(application)

        return Response(response.data)
