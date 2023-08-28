from django.shortcuts import render
from rest_framework import mixins
from rest_framework.views import APIView
from rest_framework.viewsets import ReadOnlyModelViewSet, GenericViewSet
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from .serializers import WalkInSerializer, VenueSerializer
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

    def post(self, request, format=None):
        print(request.data.dict())
        application_dict = {k: int(v) for k, v in request.data.dict().items()}
        print(application_dict)
        a = Application(**application_dict)
        a.save()
        return Response("hit")
