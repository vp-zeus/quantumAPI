from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

from users.serializers import ProfileSerializer, UserSerializer

# Create your views here.

class ProfileView(APIView):
    permission_classes = [IsAuthenticated]
    def get(self,request,format=None):
        user = ProfileSerializer(request.user.profile)
        return Response(user.data)
