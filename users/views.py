from cProfile import Profile
import profile
from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.parsers import JSONParser

from users.serializers import EducationalQualificationSerializer, ProfileSerializer, UserSerializer

# Create your views here.


class UserView(APIView):
    parser_classes = [JSONParser]

    def post(self, request):
        serializer = UserSerializer(
            data=request.data, context={'request': request})

        serializer.is_valid()

        profile = serializer.save()
        response = ProfileSerializer(profile)

        return Response(response.data)


class ProfileView(APIView):
    permission_classes = [IsAuthenticated]
    parser_classes = [JSONParser]

    def get(self, request, format=None):
        user = ProfileSerializer(request.user.profile)
        profile = request.user.profile
        education = profile.educational_qualification
        return Response(user.data)


class QualificationView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        profile = request.user.profile
        education = profile.educational_qualification
        print(education)

        return Response("hit")
