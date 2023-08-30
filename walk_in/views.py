from email.mime import application
import json
from django.shortcuts import render
from rest_framework import mixins
from rest_framework.views import APIView
from rest_framework.generics import RetrieveAPIView
from rest_framework.viewsets import ReadOnlyModelViewSet, GenericViewSet
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.parsers import MultiPartParser, FormParser
from users.models import College, Degree, Stream

from users.serializers import CollegeSerializer, DegreeSerializer, StreamSerializer
from .serializers import ApplicationSerializer, RoleSerializer, WalkInSerializer, VenueSerializer
from .models import Application, Role, WalkIn, Venue

from common.permissions import OwnApplicationPermission

# Create your views here.


class WalkInViewSet(ReadOnlyModelViewSet):
    serializer_class = WalkInSerializer
    queryset = WalkIn.objects.all()


class RoleViewSet(ReadOnlyModelViewSet):
    serializer_class = RoleSerializer
    queryset = Role.objects.all()


class DegreeeViewSet(ReadOnlyModelViewSet):
    serializer_class = DegreeSerializer
    queryset = Degree.objects.all()


class StreamViewSet(ReadOnlyModelViewSet):
    serializer_class = StreamSerializer
    queryset = Stream.objects.all()


class CollegeViewSet(ReadOnlyModelViewSet):
    serializer_class = CollegeSerializer
    queryset = College.objects.all()


class VenueViewSet(mixins.RetrieveModelMixin, GenericViewSet):
    serializer_class = VenueSerializer
    queryset = Venue.objects.all()


class ApplicationView(APIView):
    permission_classes = [IsAuthenticated]
    parser_classes = [MultiPartParser, FormParser]

    def post(self, request):
        # preferred_roles = request.data['preferred_roles']
        request.data["preferred_roles"] = json.loads(
            request.data["preferred_roles"])
        serializer = ApplicationSerializer(data=request.data.dict())
        profile = request.user.profile
        serializer.is_valid(raise_exception=True)

        application = serializer.save(profile=profile)

        response = ApplicationSerializer(application)

        return Response(response.data)


class ApplicationDetailView(RetrieveAPIView):
    queryset = Application.objects.all()
    serializer_class = ApplicationSerializer
    permission_classes = [IsAuthenticated, OwnApplicationPermission]
