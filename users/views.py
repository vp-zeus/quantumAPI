import json
from django.shortcuts import render
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ReadOnlyModelViewSet
from rest_framework.parsers import JSONParser, MultiPartParser, FormParser
from users.models import Skill

from users.serializers import EducationalQualificationSerializer, ProfileSerializer, SkillSerializer, UserSerializer

# Create your views here.


class UserView(APIView):
    parser_classes = [MultiPartParser, FormParser]

    def post(self, request):
        try:
            raw_data = request.data['raw_data']
            parsed_data = json.loads((raw_data))
            parsed_data["profile"]["profile_pic"] = request.data['profile_pic']
            parsed_data["profile"]["resume"] = request.data['resume']
        except:
            return Response({
                "detail": "Malformed request body!"
            }, 401)

        serializer = UserSerializer(
            data=parsed_data, context={'data': parsed_data})

        serializer.is_valid()
        profile = serializer.save()
        response = ProfileSerializer(profile)

        return Response(response.data)
        # return Response('hit')


class ProfileView(APIView):
    permission_classes = [IsAuthenticated]
    parser_classes = [JSONParser]

    def get(self, request, format=None):
        user = ProfileSerializer(request.user.profile)
        return Response(user.data)


class QualificationView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        profile = request.user.profile
        education = profile.educational_qualification

        return Response("hit")


class SkillViewSet(ReadOnlyModelViewSet):
    serializer_class = SkillSerializer
    queryset = Skill.objects.all()
