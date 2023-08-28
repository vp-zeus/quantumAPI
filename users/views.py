from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.parsers import JSONParser

from users.serializers import ProfileSerializer, UserSerializer

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
        return Response(user.data)
